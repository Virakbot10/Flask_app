from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, redirect, render_template, session, url_for, jsonify
from flask_cors import CORS
from flask_session import Session
import requests

appConf = {
    "OAUTH2_CLIENT_ID": "flask_app",
    "OAUTH2_CLIENT_SECRET": "8QqPTy9PKvTI6WB3FVy7sDiZQ8eRYHX9",
    "OAUTH2_ISSUER": "http://localhost:8080/realms/myrealm",
    "FLASK_SECRET": "ALongRandomlyGeneratedString",
    "FLASK_PORT": 5000
}

app = Flask(__name__)
app.secret_key = appConf.get("FLASK_SECRET")
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

CORS(app, supports_credentials=True)

oauth = OAuth(app)
oauth.register(
    "myApp",
    client_id=appConf.get("OAUTH2_CLIENT_ID"),
    client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
        # 'code_challenge_method': 'S256'  # enable PKCE
    },
    server_metadata_url=f'{appConf.get("OAUTH2_ISSUER")}/.well-known/openid-configuration',
)

def is_token_active(access_token):
    introspection_endpoint = oauth.myApp.server_metadata.get("introspection_endpoint")
    if not introspection_endpoint:
        return True
    data = {
        'token': access_token,
        'client_id': appConf.get("OAUTH2_CLIENT_ID"),
        'client_secret': appConf.get("OAUTH2_CLIENT_SECRET")
    }
    response = requests.post(introspection_endpoint, data=data)
    if response.status_code == 200:
        result = response.json()
        return result.get("active", False)
    return False

@app.route("/")
def home():
    if "user" in session:
        return jsonify(session["user"])
    else:
        return redirect(url_for("login"))

@app.route("/callback")
def callback():
    try:
        app.logger.info(f"State before callback: {session.get('state')}")
        token = oauth.myApp.authorize_access_token()
        session["user"] = token
        app.logger.info(f"State after callback: {session.get('state')}")
        return redirect('http://localhost:5173/') # redirect to frontend
    except Exception as e:
        app.logger.error(f"Error during callback: {e}")
        return jsonify({"error": str(e)}), 400

@app.route("/login")
def login():
    # check if session already present
    if 'user' in session:
        return redirect(url_for("home"))
    app.logger.info(f'Redirecting to authorize URL: {url_for("callback", _external=True)}')
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("callback", _external=True))

@app.route("/loggedOut")
def loggedOut():
    # check if session already present
    if 'user' in session:
        abort(404)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    if 'user' in session:
        id_token = session["user"]["id_token"]
        session.clear()
        return redirect(
            appConf.get("OAUTH2_ISSUER")
            + "/protocol/openid-connect/logout?"
            + urlencode(
                {
                    "post_logout_redirect_uri": url_for("loggedOut", _external=True),
                    "id_token_hint": id_token
                },
                quote_via=quote_plus,
            )
        )
    else:
        return redirect(url_for("home"))
    
@app.route("/api/userinfo")
def userinfo():
    if 'user' in session:
        token = session['user']
        access_token = token["access_token"]
        if not is_token_active(access_token):
            session.clear()
            return jsonify({"error": "Session expired or token revoked"}), 401
        return jsonify(token)
    else:
        return jsonify({"error": "Not logged in"}), 401
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=appConf.get("FLASK_PORT", 5000), debug=True)
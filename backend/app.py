import requests
from flask import Flask, redirect, url_for, session, request, render_template
import logging
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = '123456'

logging.basicConfig(level=logging.DEBUG) # enable logging

keycloak_server_url = 'http://localhost:8080/'
realm_name = 'myrealm'
client_id = 'flask_app'
client_secret = '1HFXRLeZfNxBWJYT9lLG3IS9JukaxT1I'

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    else:
        return redirect(url_for('login'))
    
@app.route('/login')
def login():
    authorize_url = f'{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/auth'
    redirect_uri = 'http://localhost:5000/callback'
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': 'openid profile email'
    }
    query = urlencode(params)
    return redirect(f"{authorize_url}?{query}")  # Use encoded query

@app.route('/callback')
def callback():
    code = request.args.get('code')

    logging.debug(f'Code: {code}')
    
    token_endpoint = f'{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:5000/callback',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_endpoint, data=payload)
    token_data = response.json()

    if 'access_token' in token_data:
        userinfo_endpoint = f'{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/userinfo'
        userinfo_response = requests.get(userinfo_endpoint, headers={'Authorization': f'Bearer {token_data["access_token"]}'})
        user_info = userinfo_response.json()

        session['user'] = {
            'id_token': token_data.get('id_token'),
            'access_token': token_data.get('access_token'),
            'refresh_token': token_data.get('refresh_token'),
            'username': user_info.get('preferred_username'),
            'email': user_info.get('email')
        }

        logging.debug("User logged in successfully")
        return redirect(url_for('index'))
    else:
        logging.error("Failed to fetch tokens.")
        return 'Failed to fetch tokens.'

@app.route('/logout')
def logout():
    logging.debug('Attempting to log out user.')

    try:
        
        session.clear() # Clear session data upon successful logout
        
        end_session_endpoint = f'{keycloak_server_url}/realms/{realm_name}/protocol/openid-connect/logout'
        redirect_uri = 'http://localhost:5000/login'

        # Optionally add 'id_token_hint' to request to invalidate sessoin at IdP
        response = requests.get(f"{end_session_endpoint}?redirect_uri={redirect_uri}", timeout=5)

        logging.debug('Session cleared. Redirecting to login page.')

        return redirect(url_for('login'))
    except Exception as e:
        logging.error(f'Failed to log out user: {e}')
        return 'Failed to log out user. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
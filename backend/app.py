# app.py
from flask import Flask, request, jsonify
import jwt  # PyJWT
import requests

app = Flask(__name__)

def get_keycloak_public_key():
    keycloak_realm_url = 'http://localhost:8080/realms/myrealm'
    response = requests.get(keycloak_realm_url)
    response.raise_for_status()
    keycloak_public_key = response.json().get("public_key")
    # Convert the key to PEM format:
    pem_key = f"-----BEGIN PUBLIC KEY-----\n{keycloak_public_key}\n-----END PUBLIC KEY-----"
    return pem_key

@app.route('/api/protected', methods=['GET'])
def protected():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Missing token"}), 401

    try:
        token = auth_header.split(" ")[1]
    except IndexError:
        return jsonify({"error": "Invalid token format"}), 401

    public_key = get_keycloak_public_key()

    try:
        # Adjust the 'audience' value if necessary; here it should match your Keycloak client ID.
        decoded = jwt.decode(token, public_key, algorithms=["RS256"], audience="account")
        return jsonify({
            "message": "Access granted",
            "user": decoded.get("preferred_username"),
            "token_claims": decoded
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError as e:
        app.logger.error(f"Token verification failed: {e}")
        return jsonify({"error": f"Invalid token: {str(e)}"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)

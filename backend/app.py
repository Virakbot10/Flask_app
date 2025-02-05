import requests
from flask import Flask, redirect, url_for, session, request, jsonify, render_template
import logging
from urllib.parse import urlencode
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-seceret')
CORS(app, supports_credentials=True, origins=os.getenv('CORS_ORIGINS', 'http://localhost:5173'))

logging.basicConfig(level=logging.DEBUG) # enable logging

KEYCLOAK_URL = os.getenv('KEYCLOAK_URL', 'http://localhost:8080/')
REALM = os.getenv('KEYCLOAK_REALM', 'myrealm')
CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'flask-app')
CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRE','1HFXRLeZfNxBWJYT9lLG3IS9JukaxT1I')
    
@app.route('/api/login')
def login():
    auth_url = f'{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/auth'
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': 'http://localhost:5000/api/callback',
        'response_type': 'code',
        'scope': 'openid profile email'
    }
    return redirect(f"{auth_url}?{urlencode(params)}")

@app.route('/api/callback')
def callback():
    code = request.args.get('code')

    logging.debug(f'Code: {code}')
    if not code:
        return jsonify({'error': 'Missing authorization code'}), 400
    
    token_url = f'{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token'
        
    try:
        # Exchange authorization code for tokens
        response = requests.post(token_url, data={
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': 'http://localhost:5000/api/callback'
        })
        response.raise_for_status()
        tokens = response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Token request failed: {str(e)}")
        return jsonify({'error': 'Authentication failed'}), 401
    except ValueError:
        logging.error("Invalid JSON response from Keycloak")
        return jsonify({'error': 'Authentication failed'}), 401

    if 'access_token' not in tokens:
        logging.error("Access token missing in response")
        return jsonify({'error': 'Authentication failed'}), 401

    # Store tokens in session
    session.update({
        'access_token': tokens['access_token'],
        'refresh_token': tokens.get('refresh_token', None),  # Safe .get() usage
        'id_token': tokens.get('id_token', None)
    })

    # Get user info
    try:
        userinfo_response = requests.get(
            f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/userinfo",
            headers={'Authorization': f'Bearer {session["access_token"]}'}
        )
        userinfo_response.raise_for_status()
        user_info = userinfo_response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Userinfo request failed: {str(e)}")
        return jsonify({'error': 'Failed to fetch user info'}), 401

    # Store user info in session
    session['user'] = {
        'username': user_info.get('preferred_username'),
        'email': user_info.get('email')
    }

    return redirect(os.getenv('FRONTEND_URL', 'http://localhost:5173'))

@app.route('/api/user')
def get_user():
    """Get current user info"""
    if 'user' not in session:
        return jsonify({'authenticated': False}), 200
    
    return jsonify({
        'authenticated': True,
        'username': session['user'].get('username'),
        'email': session['user'].get('email')
    })

@app.route('/api/logout')
def logout():
    logging.debug('Attempting to log out user.')

    """Logout from Keycloak"""
    if 'id_token' not in session:
        return jsonify({'message': 'Not logged in'}), 400

    # Clear Flask session first
    session.clear()

    # Keycloak logout URL
    logout_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/logout"
    params = {
        'id_token_hint': session.get('id_token'),
        'post_logout_redirect_uri': os.getenv('FRONTEND_URL', 'http://localhost:5173')
    }

    return redirect(f"{logout_url}?{urlencode(params)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
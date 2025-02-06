from flask import Flask, redirect, session, url_for, jsonify, request
from flask_oidc import OpenIDConnect
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')

# Configure OIDC
app.config.update({
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_SCOPES': ['openid', 'profile', 'email'],
    'OIDC_CALLBACK_ROUTE': '/oidc/callback',
    'OVERWRITE_REDIRECT_URI': os.getenv('FRONTEND_URL', 'http://localhost:5173'),
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'SECRET_KEY': os.getenv('FLASK_SECRET_KEY', 'supersecretkey'),
    'PERMANENT_SESSION_LIFETIME': 3600,
    'SESSION_COOKIE_SECURE': False,  # Set to True in production
    'SESSION_COOKIE_SAMESITE': 'Lax',
    'SESSION_COOKIE_HTTPONLY': True
})

oidc = OpenIDConnect(app)

@app.route('/api/login')
def login():
    """Initiate Keycloak login flow"""
    if oidc.user_loggedin:
        # If already logged in, redirect to the frontend
        return redirect(os.getenv('FRONTEND_URL', 'http://localhost:5173'))
    
    # Redirect to Keycloak login page
    return oidc.redirect_to_auth_server(url_for('oidc_callback', _external=True))

@app.route('/oidc/callback')
@oidc.require_login
def oidc_callback():
    """Keycloak OIDC callback handler"""
    # Store user info in session
    session['user'] = {
        'username': oidc.user_getfield('preferred_username'),
        'email': oidc.user_getfield('email')
    }
    # Redirect to the frontend after successful login
    return redirect(os.getenv('FRONTEND_URL', 'http://localhost:5173'))

@app.route('/api/user')
def user_info():
    """Get current user information"""
    if not oidc.user_loggedin:
        return jsonify({'authenticated': False}), 200
    
    return jsonify({
        'authenticated': True,
        'username': session.get('user', {}).get('username'),
        'email': session.get('user', {}).get('email')
    })

@app.route('/api/logout')
def logout():
    """Logout from Keycloak"""
    if oidc.user_loggedin:
        post_logout_uri = os.getenv('FRONTEND_URL', 'http://localhost:5173')
        logout_url = (
            f"{oidc.client_secrets['issuer']}/protocol/openid-connect/logout"
            f"?post_logout_redirect_uri={post_logout_uri}"
            f"&id_token_hint={oidc.get_id_token()}"
        )
        oidc.logout()
        session.clear()
        return redirect(logout_url)
    return redirect(url_for('user_info'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
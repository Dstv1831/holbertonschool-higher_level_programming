#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'SecretKey'
jwt = JWTManager(app=app)

# .get("username") -> returns the value of that Key
# using get() is a good practice, but since you’re sure the keys exist, it's not strictly necessary.
# .values() -> returns the values of all keys in a dictionary
# .items() -> returns a view object with a list of tuples caontinein key-value pairs

users = {
        "user1": {
            "username": "David",
            "password": generate_password_hash("abc123"),
            "role": "user"
            },
        "user2": {
            "username": "Jacob",
            "password": generate_password_hash("DEF567"),
            "role": "admin"
            }
    }

@auth.verify_password
def verify_password(username, password):
    for user in users.values():
        if user['username'] == username and \
            check_password_hash(user['password'], password=password):
            return user
    return None

@app.route("/basic-protected")
@auth.login_required
def access():
    """Basic Authentication"""
    return jsonify(message="Basic Auth: Access granted")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
     # Check if username and password are provided
    if not username or not password:
        return jsonify(error="Username and password required"), 400
    
    for key, user_data in users.items():
        if user_data["username"] == username and check_password_hash(user_data['password'], password):
            # Successfully authenticated, create access token
            access_token = create_access_token(identity={"username": username, "role": user_data['role']})
            return jsonify(access_token=access_token)

    # Invalid credentials
    return jsonify(error="Invalid credentials"), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted")

# Custom error handlers for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify(error="Missing or invalid token"), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify(error="Invalid token"), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify(error="Token has expired"), 401

if __name__ == "__main__":
    app.run()
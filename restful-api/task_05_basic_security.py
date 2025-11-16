#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "fqY[[4VQwSub!r+r;LMwQ$CrmmAQ=/Maw>.(-n3R#]E"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if (username in users and check_password_hash(users[username]["password"], password)):
        return (users[username])
    return False

@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    return ("Basic Auth: Access Granted")

@app.post("/login")
def login():
    user = users.get(request.json["username"])
    if (user and check_password_hash(user["password"], request.json.get("password"))):
        return (jsonify({"access_token": create_access_token(identity=user["username"], additional_claims={"role": user["role"]})}))
    return (jsonify({"error": "Invalid credentials"}), 401)

@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    return ("JWT Auth: Access Granted")

@app.get("/admin-only")
@jwt_required()
def admin_only():
    user = users.get(get_jwt_identity())
    if (user and user["role"] == "admin"):
        return ("Admin Access: Granted")
    return (jsonify({"error": "Admin access required"}), 403)

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
	return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
	return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
	return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
	return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
	return jsonify({"error": "Fresh token required"}), 401

if (__name__ == "__main__"):
    app.run()

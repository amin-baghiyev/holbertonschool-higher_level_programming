#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return ("Welcome to the Flask API!")

@app.route("/data")
def data():
    return (jsonify(list(users.keys())))

@app.route("/status")
def status():
    return ("OK")

@app.route("/users/<username>")
def get_user(username):
    if (username not in users):
        return (jsonify({"error": "User not found"}), 404)
    return (jsonify(users[username]))

@app.post("/add_user")
def add_user():
    if (request.json is None):
        return (jsonify({"error":"Invalid JSON"}), 400)
    if ("username" not in request.json):
        return (jsonify({"error":"Username is required"}), 400)
    if (request.json["username"] in users):
        return (jsonify({"error":"Username already exists"}), 409)
    users[request.json["username"]] = request.json
    return (jsonify({"message": "User added", "user": users[request.json["username"]]}))

if (__name__ == "__main__"):
    app.run()

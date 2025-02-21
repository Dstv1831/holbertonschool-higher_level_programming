#!/usr/bin/python3

from flask import Flask, jsonify, request

users = {}

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    client = list(users)
    return jsonify(client)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<user_name>")
def details(user_name):
    user = users.get(user_name)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add():
        # Parses the incoming JSON request data and converts it into a Python dictionary
    info = request.get_json()
    if not info or "username" not in info:
        return jsonify({"error": "Username is required"}), 400
    
    username = info["username"]
    users[username] = info
    return (jsonify({
        "message": "User added",
        "user": info
        }), 201)

if __name__ == "__main__":
    app.run()
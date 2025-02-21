#!/usr/bin/python3

from flask import Flask, jsonify, request

users = {"Jane": {"Username": "Jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "David": {"Username": "DSTV", "name": "Santiago", "age": 30, "city": "Melbourne"},
         "Nicolas": {"Username": "Nico", "name": "Eduardo", "age": 32, "city": "Jenna"}
        }

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
def info(user_name):
    user = users.get(user_name)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add():
        data = request.get_json()
        if not data or "username" not in data:
            return jsonify({"error": "Username is required"}), 400
        
        username = data["username"]
        users[username] = data
        return (jsonify({
            "message": "User added",
            "user": data
            }), 201)

if __name__ == "__main__":
    app.run()
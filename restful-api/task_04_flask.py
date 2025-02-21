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
    if user_name not in list(users):
         return jsonify({"error": "User not found"})
    user = users[user_name]
    return jsonify(user)

@app.route("/add_user", methods=['GET','POST'])
def add():
    # if request.method == 'POST':
        new_user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
        users["username"] = new_user
        return (jsonify({
            "message": "User added",
            "user": new_user
            }), 201)

if __name__ == "__main__":
    app.run()
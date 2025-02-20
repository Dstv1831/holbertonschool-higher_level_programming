#!/usr/bin/python3

from flask import Flask, jsonify

users = {"Jane": {"Username": "Jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "David": {"Username": "DSTV", "name": "Santiago", "age": 30, "city": "Melbourne"}
        }

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API"

@app.route("/data")
def data():
    return jsonify(users)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def info(username):
    user = users[username]
    return jsonify(users)

if __name__ == "__main__":
    app.run()
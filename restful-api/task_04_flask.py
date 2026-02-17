#!/usr/bin/python3
"""
Simple RESTful API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (DO NOT add test data)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data by username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()

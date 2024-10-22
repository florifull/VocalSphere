from flask import Flask, jsonify, request, session
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
# Set the secret key to sign the session cookie
app.secret_key = os.getenv("SECRET_KEY")

# Connect to MongoDB using the URI from .env
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["social_media_app"]
users_collection = db["users"]

# Enable CORS
CORS(app)


# Route to signup
@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username")
    password = request.json.get("password")

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if the username already exists
    if users_collection.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 400

    # Insert the new user into the database
    users_collection.insert_one({"username": username, "password": password})

    return jsonify({"message": "User created successfully"}), 201


# Route to login
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Find the user in the database
    user = users_collection.find_one({"username": username})

    if not user or user["password"] != password:
        return jsonify({"error": "Invalid username or password"}), 400

    # Set the user as logged in (store the username in session)
    session["username"] = username
    return jsonify({"message": "Logged in successfully"}), 200


@app.route("/logout", methods=["POST"])
def logout():
    # Clear the session
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)

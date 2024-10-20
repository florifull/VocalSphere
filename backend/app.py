import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB using pymongo
client = MongoClient(mongo_uri)

# Specify the database name
database_name = 'social_media_app'
db = client[database_name]

# Access the 'users' collection in the database
users_collection = db['users']

# Route to add data to the MongoDB collection
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # Get JSON data from request body
    users_collection.insert_one(data)  # Insert data into 'users' collection
    return jsonify({"message": "Data added to MongoDB"}), 201

# Route to retrieve all users from MongoDB collection
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())  # Retrieve all users
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(users), 200

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)

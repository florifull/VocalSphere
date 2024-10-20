from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB using the URI from .env
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["social_media_app"]
users_collection = db["users"]

# Add CORS headers manually
@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# Route to handle adding data
@app.route('/add', methods=['POST'])
def add_data():
    if request.method == 'OPTIONS':
        return make_response(jsonify({'status': 'OK'}), 200)

    data = request.json
    users_collection.insert_one(data)
    return jsonify({'message': 'User added successfully'}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)

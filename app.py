from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB Atlas
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Use a new database and collection
db = client["assignment_db"]
collection = db["todo_items"]

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/todo', methods=['GET'])
def todo_form():
    return render_template('To_Do_Form.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })
        return "Item submitted successfully!", 200
    else:
        return "Missing item name or description", 400

if __name__ == '__main__':
    app.run(debug=True)

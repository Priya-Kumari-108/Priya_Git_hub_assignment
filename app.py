
from flask import Flask, request, jsonify, render_template, render_template_string
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB Atlas
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Use a new database and collection

db = client["assignment_db"]
collection = db["todo_items"]

@app.route('/')
def home():

    return "Welcome to the Flask MongoDB TODO App!"

@app.route('/todo', methods=['GET'])
def todo_form():
    with open('To_Do_Page/To_Do_Form.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    item_id = request.form.get('itemId')
    item_uuid = request.form.get('ItemUUID')
    item_hash = request.form.get('itemHash')


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

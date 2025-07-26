from flask import Flask, request, render_template, render_template_string
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Database and collection
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

    if not item_name or not item_description:
        return "Both name and description are required!", 400

    # Insert item into MongoDB
    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return "Item submitted successfully!", 200

if __name__ == '__main__':
    app.run(debug=True)

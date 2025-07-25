from flask import Flask, jsonify, request, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

# Route to serve the To-Do HTML form
@app.route('/todo', methods=['GET'])
def todo_form():
    with open('To_Do_Page/To_Do_Form.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

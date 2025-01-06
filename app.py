from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# CORS configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route("/")
def say_hello():
    return "Hello World"

@app.route("/data")
def send_data():
    return jsonify({"success": True, "message": "hello from flask"})

if __name__ == "__main__":
    app.run(debug=True)

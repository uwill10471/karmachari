from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
from auth import auth_bp
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(auth_bp , url_prefix='/auth')

# CORS configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Set secure cookie options
app.config.update(
SESSION_COOKIE_SECURE=True, # Only send cookies over HTTPS
SESSION_COOKIE_HTTPONLY=True, # Prevent JavaScript access to cookies
SESSION_COOKIE_SAMESITE='Lax', # Help prevent CSRF attacks
)

@app.route("/")
def say_hello():
    return "Hello World"

@app.route("/data")
def send_data():
    return jsonify({"success": True, "message": "hello from flask"})

if __name__ == "__main__":
    app.run(debug=True)

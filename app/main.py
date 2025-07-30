from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    app.logger.info("Home route accessed")
    return jsonify({"message": "Hello from DevOps Flask app!"})

@app.route('/health')
def health():
    app.logger.info("Health check route accessed")
    return jsonify({"status": "UP"})

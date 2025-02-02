from flask import Flask, jsonify
from prometheus_client import start_http_server, Counter
import pymongo

app = Flask(__name__)
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

# MongoDB connection
client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["mydb"]
collection = db["mycollection"]

@app.route('/')
def root():
    return "Welcome to the Python Backend!", 200

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest(), 200

@app.route('/data')
def get_data():
    REQUEST_COUNT.inc()
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200

if __name__ == '__main__':
    start_http_server(5001)  # Expose metrics on port 5001
    app.run(host='0.0.0.0', port=5000)
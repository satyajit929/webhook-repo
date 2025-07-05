from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['webhook_db']
collection = db['payloads']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    data = request.json
    if data:
        collection.insert_one(data)
        return jsonify({'message': 'Payload received and stored'}), 200
    return jsonify({'error': 'Invalid payload'}), 400

if __name__ == '__main__':
    app.run(debug=True)

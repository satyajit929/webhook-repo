from flask import Flask, request, jsonify, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# MongoDB Atlas connection
uri = "mongodb+srv://webhookuser:webhook123@cluster1.9b1rfcz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['webhook_db']
collection = db['payloads']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook/receiver', methods=['GET', 'POST'])  # Allow GET for browser test
def webhook_receiver():
    if request.method == 'GET':
        return "✅ Webhook is live and listening for POST data."

    data = request.json
    if data:
        collection.insert_one(data)
        return jsonify({'message': 'Payload received and stored'}), 200
    return jsonify({'error': 'Invalid payload'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ✅ Fixed: removed comma

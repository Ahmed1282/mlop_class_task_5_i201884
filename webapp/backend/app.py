from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client['webappdb']

# Explicitly create the 'users' collection if it doesn't exist
if 'users' not in db.list_collection_names():
    db.create_collection('users')

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if name and email:
        db.users.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data submitted successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required fields'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

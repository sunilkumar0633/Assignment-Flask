from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo
from bson import json_util
import json

load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.ass
collection=db['Assignment']
app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5050', debug = True)
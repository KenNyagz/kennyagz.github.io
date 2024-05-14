from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
#CORS(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})


client = MongoClient("mongodb://localhost:27017/")
db = client['test']
collection = db['testCollection']

@app.route("/patients/create", methods=["POST"])
def create():
    #user = request.form['user']
    #_id = request.form['id']
    user = request.json['user']
    _id = request.json['id']

    entry = { "user": user, "id": _id}
    result = collection.insert_one(entry)
    print('yes')
    return jsonify({"id": str(result.inserted_id)})

if __name__ == "__main__":
    app.run(port=5500, debug=True)

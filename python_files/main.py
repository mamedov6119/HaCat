from http import client
from dotenv import load_dotenv, find_dotenv
import os
import pprint
import pymongo 
from pymongo import MongoClient
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin
load_dotenv(find_dotenv())


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client["mamedov6119"]
col = db["users"]

app = Flask(__name__)
CORS(app)

import users_coll, pc_parts # function from users @app.route("/<name>") def user(name):

if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)





from flask import Flask
from os import environ as env
from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['nursenav']
users = db['users']
nurses = db['nurses']

@app.route("/")
def get_index():
    users.insert_one({"name":"test"})
    return "helloworld"


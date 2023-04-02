from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory
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
    return render_template("index.html")

@app.route('/<directory>/<path>')
def send_static_styles(directory, path):
    return send_from_directory('static/' + directory, path)

@app.route("/login")
def get_login():
    pass

@app.route("/logout")
def get_logout():
    pass

@app.route("/search")
def search():
    pass

@app.route("/profile", methods=['GET', 'POST'])
def get_profile():
    pass

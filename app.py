from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory
from dbmongo import *

env = get_env()

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")



@app.route("/")
def get_index():
    return render_template("index.html", tags=all_tags())

@app.route("/nurse", methods=['POST'])
def get_nurses():
    location = request.form['location']
    tags = request.form['tags']
    return find_nurses(location, tags)

@app.route('/<directory>/<path>')
def send_static_styles(directory, path):
    return send_from_directory('static/' + directory, path)

@app.route("/login")
def get_login():
    pass

@app.route("/logout")
def get_logout():
    pass

@app.route("/profile", methods=['GET', 'POST'])
def get_profile():
    pass

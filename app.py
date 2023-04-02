from dbmongo import *
from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory
from flask_bcrypt import Bcrypt
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, logout_user, current_user
from flask import Flask, render_template, url_for
from pymongo import MongoClient
from flask_pymongo import PyMongo


app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['nursenav']
details = db['details']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['nursenav']
details = db['details']


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_details = details.find_one({"name": username.data})

        if existing_details:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template("index.html", tags=all_tags(), MAPBOX_KEY=env.get("MAPBOX_KEY"))


@app.route('/<directory>/<path>')
def send_static_styles(directory, path):
    return send_from_directory('static/' + directory, path)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        existing_details = details.find_one({"name": form.username.data})
        if existing_details:
            if bcrypt.check_password_hash(existing_details["password"], form.password.data):
                return redirect(url_for('register'))
        else:
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        details.insert_one(
            {"name": form.username.data, "password": hashed_password})

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

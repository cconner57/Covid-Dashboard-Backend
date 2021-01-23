from flask import Flask, request, redirect, render_template, flash, session
from flask_cors import CORS
from models import db, connect_db, User
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Covid-19'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "A secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request_json = request.get_json()
        email = request_json.get('email')
        password = request_json.get('password')
        user = User.authenticate(
            email = email,
            password = password
        )
        if user: 
            return 'Successful Login'
        return ('Failed Login', 401)

@app.route('/signup', methods=['POST'])
def signup():
    request_json = request.get_json()
    email = request_json.get('email')
    password = request_json.get('password')
    user = User.signup(
        email = email,
        password = password
    )
    db.session.commit()
    return redirect('/')

@app.route('/404')
def show_404():
    """404 Error Page."""

    return render_template("404.html")
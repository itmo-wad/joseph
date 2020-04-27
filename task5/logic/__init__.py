from flask_sslify import SSLify as ssl
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask import Flask
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad_task5"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(16)
login = LoginManager(app)
mongo = PyMongo(app)
sslify = ssl(app)

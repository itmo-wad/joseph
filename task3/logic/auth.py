from flask import Blueprint, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user
from flask_login import logout_user
from .user import User

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    userFname = request.form.get('userFname')
    userLname = request.form.get('userLname')
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    # print(userPass + ' ' + userEmail + ' ' + userFname + ' ' + userLname)
    if userFname and userLname and userEmail and userPass:
        return redirect(url_for("index"))
    return redirect(url_for("register"))


@auth.route('/login', methods=['POST'])
def login():
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    user = User(userEmail, userPass).get(userEmail)
    print(user)
    if user is not None:
        flash('Logged in successfully.')
        login_user(user)
        return redirect(url_for("cabernet"))
    return redirect(url_for("index"))

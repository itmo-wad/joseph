from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, redirect, url_for, redirect
from logic import app, login
from flask import flash
from .user import User
from . import db_crud

#Mandatory function For flask-login
@login.user_loader
def user_loader(email):
    l_user = db_crud.findByEmail(email)
    if l_user is None:
        return
    user = User()
    user.id = email
    return user

#Mandatory function For flask-login
@login.request_loader
def request_loader(request):
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    l_user = db_crud.findByEmail(userEmail)
    if l_user is None:
        return

    user = User()
    user.id = userEmail
    user.is_authenticated = check_password_hash(l_user['pswd'], userPass)
    return user


@app.route('/signup', methods=['POST'])
def signup():
    userFname = request.form.get('userFname')
    userLname = request.form.get('userLname')
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    if userFname and userLname and userEmail and userPass:
        new_user = {
			"_id": userFname + ' ' + userLname,
			"mail": userEmail,
            "uname": userFname,
			"pswd": generate_password_hash(userPass)
    	}
        db_crud.userOneInsert(new_user)
        return redirect(url_for("cabernet"))
    return redirect(url_for("register"))


@app.route('/login', methods=['POST'])
def login():
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    root = db_crud.findByEmail(userEmail)
    if root is not None and check_password_hash(root['pswd'], userPass):
        user = User()
        user.id = userEmail
        login_user(user)
        flash('Logged in as: ' + current_user.id)
        return redirect(url_for("cabernet"))
    return redirect(url_for("index"))


# Unauthorized Access Handling
# @login.unauthorized_handler
# def unauthorized_handler():
#     # return redirect(url_for("index"))
#     return "WTF !!"


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

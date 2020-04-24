from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from .user import User, user_database

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    userFname = request.form.get('userFname')
    userLname = request.form.get('userLname')
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    # print(userPass + ' ' + userEmail + ' ' + userFname + ' ' + userLname)
    if userFname and userLname and userEmail and userPass:
        new_user = {
            userEmail: {
    			"name": userFname + ' ' + userLname,
    			"mail": userEmail,
                "uname": userFname,
    			"pswd": generate_password_hash(userPass)
            }
    	}
        user_database['User'].update(new_user)
        return redirect(url_for("index"))
    return redirect(url_for("register"))


@auth.route('/login', methods=['POST'])
def login():
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    if userEmail in user_database['User']:
        root = user_database['User'][userEmail]
        if check_password_hash(root['pswd'], userPass):
            user = User()
            user.id = userEmail
            login_user(user)
            return redirect(url_for('auth.protected'))
    return redirect(url_for("index"))


@auth.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

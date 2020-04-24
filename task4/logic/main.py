import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, send_from_directory
from flask import redirect, url_for, make_response, jsonify
from flask_sslify import SSLify as ssl
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_required, current_user
from .auth import auth
from . import user as u


app = Flask(__name__)
login = LoginManager(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad_task4"
app.secret_key = os.urandom(16)
sslify = ssl(app)
mongo = PyMongo(app)
app.register_blueprint(auth)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('login.html')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/cabernet')
@login_required
def cabernet():
    return render_template('success.html')

# List all registerd users
@app.route('/users')
# @login_required
def list_users():
    val = mongo.db.user.find({})
    return render_template("list.html", users=val)

# Satic file route definition
@app.route('/img/<string:image>')
def rout_img(image):
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               image)

@app.route('/js/<string:script>')
def rout_js(script):
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'),
                               script)

@app.route('/css/<string:style>')
def rout_css(style):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'),
                               style)

# Unauthorized Access Handling
@login.unauthorized_handler
def unauthorized_handler():
    # return redirect(url_for("index"))
    return "WTF !!"

# Error handling 404
@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return make_response(render_template("error/404.html"), 404)

# Error handling 400
@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("error/400.html"), 400)

# Error handling 500
@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(render_template("error/500.html"), 500)

#Mandatory function For flask-login
@login.user_loader
def user_loader(email):
    l_user = mongo.db.user.find_one({'mail': email})
    if l_user is None:
        return
    user = u.User()
    user.id = email
    return user

#Mandatory function For flask-login
@login.request_loader
def request_loader(request):
    userEmail = request.form.get('userEmail')
    userPass = request.form.get('userPass')
    l_user = mongo.db.user.find_one({'mail': userEmail})
    if l_user is None:
        return

    user = u.User()
    user.id = userEmail
    user.is_authenticated = check_password_hash(l_user['pswd'], userPass)
    return user

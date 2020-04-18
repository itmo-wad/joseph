import os
from flask import Flask, render_template, send_from_directory
from flask import redirect, url_for
from flask import url_for, make_response
from flask_sslify import SSLify as ssl
from flask_login import LoginManager, login_required
from logic import auth
from logic import user as u

app = Flask(__name__)
login = LoginManager(app)
app.secret_key = os.urandom(16)
sslify = ssl(app)
from logic import auth
app.register_blueprint(auth.auth)


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

@login.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None

if __name__ == '__main__':
    app.run(debug=True)

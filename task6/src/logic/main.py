from flask import Flask, render_template, send_from_directory, redirect
from flask import url_for, make_response, request, Response
from . import actions, auth
from logic import app
import os


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        actions.write_json(msg)
        return Response("Ok", status=200)
    if auth.current_user.is_authenticated:
        return redirect(url_for('cabernet'))
    return render_template('login.html')


@app.route('/cabernet')
@auth.login_required
def cabernet():
    return render_template('success.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        actions.upload_file(request)
    return redirect(url_for('cabernet'))


@app.route('/register', methods=['GET'])
def register():
    if auth.current_user.is_authenticated:
        return redirect(url_for('cabernet'))
    return render_template('register.html')


@app.route('/img/<string:image>/')
def rout_img(image):
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               image)


@app.route('/js/<string:script>/')
def rout_js(script):
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'),
                               script)


@app.route('/css/<string:style>/')
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

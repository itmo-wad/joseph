import os
from flask import Flask, render_template, send_from_directory
from flask import url_for, make_response
from flask_sslify import SSLify as ssl

app = Flask(__name__)
sslify = ssl(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
    # return "<h1>Mjumnir First Flask App</h1>"

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


@app.errorhandler(404)
def custom_mj_not_found(error):
    """Page not found."""
    return make_response(render_template("404.html"), 404)


#
#
# @app.errorhandler(400)
# def bad_request():
#     """Bad request."""
#     return make_response(render_template("400.html"), 400)
#
#
# @app.errorhandler(500)
# def server_error():
#     """Internal server error."""
#     return make_response(render_template("500.html"), 500)


if __name__ == '__main__':
    app.run(debug=True)

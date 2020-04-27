from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from werkzeug.utils import secure_filename
from logic import app, ALLOWED_EXTENSIONS
from requests import Session
from flask import flash
import datetime as d
import json, os



def api_call(url, parameters, headers = {'Accepts': 'application/json'}):

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        write_json(data, 'api_response.json')

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_date():
    c_date = d.datetime.now().strftime("%b %d %Y %H:%M:%S")
    return c_date


def append_txt(data, filemane='users.txt'):
    with open(filemane,"a") as fo:
        fo.write(data + '\n')


def write_json(data, filename='response.json'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(r):
    file = r.files['file']
    if file.filename == '':
        flash('No selected file')
        return
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)
        flash('File uploded')
        return
    return

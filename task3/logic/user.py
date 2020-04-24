from werkzeug.security import check_password_hash
from flask_login import UserMixin
import os

user_database = {
    'User':{
        'john@1.com': {
            'name': 'John Doe',
            'mail': 'john@1.com',
            'uname': 'John',
            'pswd': 'pbkdf2:sha256:150000$FB96URjN$86ea2a5f5435b20aa981184bb770bc5b5fb17f865ae9e2b0048bf3bed0a6f80a'
            },
        'janedoe@wad.com': {
            'name': 'Jane Doe',
            'mail': 'janedoe@wad.com',
            'uname': 'Jane',
            'pswd': 'pbkdf2:sha256:150000$HHKgHv5c$fbe8640afcd778891720b6ac261ae0272015a9308f56a21ed32ff296ce524563'
            },
        'magnie@m.com': {
            'name': 'Magnie Dess',
            'mail': 'magnie@yandex.com',
            'uname': 'Magnie',
            'pswd': 'pbkdf2:sha256:150000$32otDXGB$03734879ba6f0700af2defa70c4b182fefa1eb4281ad65a9021d408a61725a3f'
            },
        'test@t.com': {
            'name': 'Test',
            'mail': 'test@t.com',
            'uname': 'Test',
            'pswd': 'pbkdf2:sha256:150000$I7M0C4bf$406d9f83bd9777baa915b2e37299a4e53255f471e8cf7a0cfb58ad8d2fb45ad9'}
    }
}

class User(UserMixin):
    pass


def get_user(self,mail,pswd):
    if mail in user_database['User']:
        root = user_database['User'][mail]
        if check_password_hash(root['pswd'], pswd):
            return self(root['mail'], mail)
    return None

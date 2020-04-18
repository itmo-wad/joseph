from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import os

class User(UserMixin):

    user_database = {"John@1.com": ("John@1.com", "John"),
               "JaneDoe": ("JaneDoe", "Jane"),
               "Mjumnir": ('magnie@yandex.com', 'magnie'),
               "Test": ('test@test.com', '1')}

    def __init__(self, username, password):
        self.id = username
        self.password = password

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    @classmethod
    def get(cls,id):
        return cls.user_database.get(id)

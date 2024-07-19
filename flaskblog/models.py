from datetime import datetime
from flaskblog import app, db, login_manager
from flask_login import UserMixin

# from itsdangerous import TimedSerializer as Serializer # a flask  extension used to generate token
from cryptography.fernet import Fernet
import base64


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# generate token that is sent to the user email
def get_fernet_key(secret_key):
    # Ensure the key is 32 bytes long
    key = secret_key.ljust(32)[:32]
    # Encode to base64 to make it URL-safe
    return base64.urlsafe_b64encode(key.encode())


fernet_key = get_fernet_key(app.config["SECRET_KEY"])
fernet = Fernet(fernet_key)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    # generate token whenever a user forgets password and attach it to ther username
    def get_reset_token(self, expires_sec=1800):
        token_data = f"{self.id}|{expires_sec}".encode()
        token = fernet.encrypt(token_data).decode("utf-8")
        return token

    # verify the generated token
    @staticmethod
    def verify_reset_token(token):
        try:
            token_data = fernet.decrypt(token.encode()).decode("utf-8")
            user_id, expires_sec = token_data.split("|")
            # Optionally, you can add expiration handling here
        except:
            return None
        return User.query.get(user_id)

    # # Email and Password reset
    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # # method that verifies the token
    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


# classes used to create SQLAlchemy tables
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}','{self.title}','{self.date_posted}')"

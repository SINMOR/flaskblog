import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "blog.db")


class Config:
    SECRET_KEY = os.getenv("API_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("email")
    MAIL_PASSWORD = os.getenv("password")

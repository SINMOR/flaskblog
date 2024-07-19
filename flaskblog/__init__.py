import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("API_KEY", "default_secret_key")
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "blog.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("email")
app.config["MAIL_PASSWORD"] = os.getenv("password")


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail(app)


from flaskblog.users.routes import users as users_blueprint
from flaskblog.posts.routes import posts as posts_blueprint
from flaskblog.main.routes import main as main_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(main_blueprint)

from flaskblog import models


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": models.User, "Post": models.Post}

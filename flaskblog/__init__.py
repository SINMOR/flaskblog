from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

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

    return app

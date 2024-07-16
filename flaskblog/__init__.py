import os 
from dotenv import find_dotenv,load_dotenv
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)





app = Flask(__name__) 
app.config ['SECRET_KEY'] = os.getenv("API_KEY", "default_secret_key")
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,  'blog.db')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  os.getenv("email")
app.config['MAIL_PASSWORD'] = os.getenv("password")
mail = Mail(app)




from flaskblog import routes,models

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': models.User, 'Post': models.Post}

# import json
# from flaskblog import app, db
# from flaskblog.models import Post

# # Correct path to the JSON file
# json_file_path = 'D:/Machine Learning/Python/flaskblog/posts.json'

# # Read JSON file
# with open(json_file_path, 'r') as file:
#     data = json.load(file)

# # Insert data into the database
# with app.app_context():
#     for item in data:
#         post = Post(
#             title=item['title'],
#             content=item['content'],
#             user_id=item['user_id']
#         )
#         db.session.add(post)
#     db.session.commit()

# print("Data loaded successfully!")

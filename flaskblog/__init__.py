import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config ['SECRET_KEY'] = 'e23df669a5280a7d44d68eccb41e021d' 
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,  'blog.db')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes

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

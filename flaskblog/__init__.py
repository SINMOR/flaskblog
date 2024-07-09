import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config ['SECRET_KEY'] = 'e23df669a5280a7d44d68eccb41e021d' 
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir,  'blog.db')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flaskblog import routes
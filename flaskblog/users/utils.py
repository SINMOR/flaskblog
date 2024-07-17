import secrets
import os
from flask import url_for
from flaskblog import app,mail
from PIL import Image
from  flask_mail import Message


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/prof_pics', picture_fn)
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    
    
    i.save(picture_path)
    
    
    return picture_fn

# a fuction to generate token and send a message to reset password 
def send_reset_email(user):
     token =  user.get_reset_token()
     msg = Message('Password Reset Request', sender='morrisindet@gmail.com', recipients=[user.email])
     msg.body =  f''' To Reset your password, visit the following link :
{url_for('users.reset_token', token=token , _external=True ) } 

If you did not make this request simply ignore this email and no change will be made      
     
     '''
     mail.send(msg)
from PIL import Image
from flask import  render_template , url_for,flash,redirect,request,abort
from flaskblog.models import User, Post
from flaskblog import app,db,bcrypt
from flask_login import login_user, current_user,logout_user,login_required
import secrets,os


# ========================================================
# =====================REDUCE PICTURE QUALITY=============
# ========================================================
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profilePic',picture_fn)
    
    output_size = (70,70)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

from flask import Blueprint

posts = Blueprint('posts',__name__)

from PIL import Image
from flask import  render_template , url_for,flash,redirect,request,abort
from flaskblog.posts.forms import PostForm
from flaskblog.models import User, Post
from flaskblog import app,db,bcrypt
from flask_login import login_user, current_user,logout_user,login_required
import secrets,os


# ========================================================
# =====================NEW POST ROUTES====================
# ========================================================
@posts.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title = 'New Post',form=form, legend='New Post')

   
# ========================================================
# =====================POST <> ROUTES=====================
# ========================================================
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)#get post by id but if it is not possible return 404
    return render_template('post.html',title=post.title, post=post)


# ========================================================
# ====================UPDATE POSTS ROUTES=================
# ========================================================
@posts.route("/post/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post has been updated !','success')
        return redirect(url_for('posts.post',post_id=post.id))
    else :
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title = 'Update Post',form=form, legend='Update Post')


# ========================================================
# ===================DELETE POST ROUTES===================
# ========================================================
@posts.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted !','success')
    return redirect(url_for('main.home'))



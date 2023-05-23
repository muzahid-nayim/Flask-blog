from flask import Blueprint

main = Blueprint('main',__name__)

from flask import  render_template , request
from flaskblog.models import User, Post

# ========================================================
# =====================HOME ROUTES========================
# ========================================================
@main.route("/")
@main.route("/home")#this is second route to go home page 
def home():
    # posts = Post.query.all()
    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts = posts, title = 'Home') #sending arguments
 

# ========================================================
# ====================ABOUT ROUTES========================
# ========================================================
@main.route("/about")
def about():
    return render_template('about.html',title = 'About')


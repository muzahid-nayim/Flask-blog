
from flaskblog import app
from flaskblog import db
# from flaskblog.models import User, Post
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,host="0.0.0.0",port=2000)

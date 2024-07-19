
from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get(
        "page", 1, type=int
    )  # makes sure if you request a page the number is an interger
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5
    )  # access the number of posts per page and order with date posted
    return render_template("main/home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("main/about.html", title="About")


from flask import (
    render_template,
    redirect,
    request,
    url_for,
    flash,
    abort,
    Blueprint,
    current_app,
)
from flask_login import login_required, current_user
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm


posts = Blueprint(
    "posts", __name__, static_folder="static", template_folder="templates"
)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required  # make the route  accessible when logged in only
def new_post():
    form = (
        PostForm()
    )  # creates an instance from posts  template  but make sure its imported to the routes file
    if (
        form.validate_on_submit()
    ):  # a condition when the post is valid return a success message pop up
        post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash(
            f"Your post has been created ", "success"
        )  # adds flash meesage using the boostrap category/class success
        return redirect(url_for("main.home"))
    return render_template(
        "posts/create_new_post.html", title="New Post", form=form, legend="New Post"
    )


@posts.route("/post/<int:post_id>")  # routes to the post_id
def post(post_id):
    post = Post.query.get_or_404(
        post_id
    )  # returns the post_id if null it returns a 404 error
    return render_template("posts/post.html", title=post.title, post=post)


@posts.route(
    "/post/<int:post_id>/update",
    methods=["GET", "POST"],
)  # routes to  a new page that is the update page
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(
        post_id
    )  # returns the post_id if null it returns a 404 error
    if (
        post.author != current_user
    ):  # create a condition to make sure only the current_user can update a post
        abort(403)
    form = PostForm()  # creates an instance of PostForm from form.py
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("You post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        "posts/create_new_post.html",
        title="Update Post",
        form=form,
        legend="Update Post",
    )


@posts.route(
    "/post/<int:post_id>/delete", methods=["POST"]
)  # routes to  a new page that is the update page
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if (
        post.author != current_user
    ):  # create a condition to make sure only the current_user can update a post
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("main.home"))

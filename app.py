# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os
from utl import acc, blogs

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = "user"
password = "password"

@app.route("/", methods=["GET"])
def root():
    if 'user' in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

@app.route("/home", methods=["GET"])
def home():
    if 'user' in session:
        count = blogs.count()
        info = []
        for i in range(count):
            info.append(blogs.describe(i))
        return render_template(
            "home.html",
            title= "Home",
            blogs = info
            )
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "GET"):
        if 'user' in session:
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html",
                title= "Login"
                )
    elif(request.method == "POST"):
        if(acc.verify_acc(request.form['username'],request.form['password'])):
            session['user'] = request.form['username']
            flash("You have successfully logged in!")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")
            return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template(
            "register.html",
            title= "Register"
            )
    if(request.method == "POST"):
        if request.form['password'] != request.form['confirmpassword']:
            flash("Passwords do not match")
            return render_template("register.html")
        elif (acc.create_acc(request.form['username'],request.form['password'])):
            return redirect(url_for("login"))
        else:
            flash("Username already exists")
            return render_template("register.html")

@app.route("/profile", methods=["GET"])
def profile():
    if 'user' in session:
        count = blogs.count()
        info = []
        for i in range(count):
            if (session['user'] == blogs.get_user(i))
                info.append(blogs.describe(i))
        return render_template("profile.html", blogs = info)
    else:
        return redirect(url_for("login"))

@app.route("/logout", methods = ["GET","POST"])
def logout():
        # remove the username from the session if it's there
        session.pop('user', None)
        flash('You were successfully logged out!')
        return redirect(url_for('login'))

@app.route("/settings", methods = ["GET", "POST"])
def settings():
    if 'user' in session:
        return render_template("settings.html")
    else:
        return redirect(url_for("login"))
@app.route("/blog/<blog_id>", methods = ["GET","POST"])
def view_blog(blog_id):
    if 'user' in session:
        return render_template("blog.html",
            blog_id = blog_id,
            description = blog.describe(blog_id),
            content = blog.read_entries(blog_id),
            is_owner = is_owner(blog_id,session['user'])
            )
    else:
        return redirect(url_for("login"))
@app.route("/profile/create_blog")
def create_blog():
    if 'user' in session:
        return render_template("create_blog.html")
    else:
        return redirect(url_for("login"))
# @app.route("/blog/<blog_id>/entry/<entry_id>", methods = ["GET","POST"])
# def view_entry():
#     render_template("entry.html",
#     content = get_entry_content(entry_id),
#     is_owner = is_owner(blog_id,session['user']))

# @app.route("/blog/<blog_id>/create_entry", methods = ["GET","POST"])
# def yolooo():
#     return 0
# @app.route("/blog/<blog_id>/entry/edit", methods = ["GET","POST"])
# def yolo():
#     return 0

if __name__ == "__main__":
	app.debug = True
	app.run()

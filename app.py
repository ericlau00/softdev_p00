# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os
from utl import acc, blogs, entries

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
            blogs = info,
            userid = session.get('userid')
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
                )
    elif(request.method == "POST"):
        session['userid'] = acc.verify_acc(request.form['username'],request.form['password'])
        if session.get('userid') != False:
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

@app.route("/logout", methods = ["GET","POST"])
def logout():
        # remove the username from the session if it's there
        session.pop('user', None)
        flash('You were successfully logged out!')
        return redirect(url_for('login'))

@app.route("/settings", methods = ["GET", "POST"])
def settings():
    if 'user' in session:
        if(request.method == "GET"):
            return render_template("settings.html",
                                    userid = session.get('userid'))
        elif(request.method == "POST"):
            return render_template("settings.html",
                                    userid=session.get('userid'))
    else:
        return redirect(url_for("login"))

@app.route("/search", methods = ["GET", "POST"])
def search():
    if 'user' in session:
        if(request.method == "GET"):
            return render_template("search.html",
                                    userid = session.get('userid'))
        if(request.method == "POST"):
            return render_template("search.html",
                                    userid = session.get('userid'))
    else:
        return redirect(url_for("login"))

@app.route("/profile/<userid>", methods=["GET"])
def profile(userid):
    username = acc.get_username(userid)
    if 'user' in session:
        return render_template("profile.html",
                                title = username,
                                username = username,
                                user_blogs = blogs.get_user_blogs(userid),
                                is_owner = (str(session.get('userid')) == userid),
                                userid = session.get('userid')
                                )
    else:
        return redirect(url_for("login"))

@app.route("/blog/<blog_id>", methods = ["GET","POST"])
def view_blog(blog_id):
    if 'user' in session:
        #print(blogs.read_entries(blog_id)[0]['content'])
        return render_template("blog.html",
            blog_id = blog_id,
            description = blogs.describe(blog_id),
            entries = blogs.read_entries(blog_id),
            is_owner = (session.get('userid') == blogs.get_userid(blog_id)),
            userid = session.get('userid')
            )
    else:
        return redirect(url_for("login"))

@app.route("/profile/create_blog", methods =["GET","POST"])
def create_blog():
    if 'user' in session:
        if(request.method == "GET"):
            return render_template("create_blog.html",
                                    userid = session.get('userid'))
        if(request.method == "POST"):
            if request.form['blog_title'] == "" or request.form['blog_title'].isspace():
                flash("please input a blog title")
                return redirect(url_for("create_blog"))
            blogs.create_blog(session.get('userid'), request.form['blog_title'])
            flash("You have successfully created a blog!")
            return redirect(url_for("profile", userid = session.get('userid')))
    else:
        return redirect(url_for("login"))

@app.route("/blog/<blog_id>/create_entry", methods = ["GET","POST"])
def create_entry(blog_id):
    if 'user' in session:
        if(request.method == "GET"):
            return render_template("create_entry.html",
                                    blog_id= blog_id,
                                    userid = session.get('userid')
                                    )
        elif(request.method == "POST"):
            if request.form['entry_content'] == '' or request.form['entry_content'].isspace():
                flash("please input some text")
                return render_template("create_entry.html",
                                        blog_id=blog_id,
                                        userid = session.get('userid'))
            entries.create_entry(blog_id, request.form['entry_content'])
            flash("You have successfully created an entry!")
            return redirect(url_for("view_blog", blog_id = blog_id))
    else:
        return redirect(url_for("login"))

@app.route("/blog/<blog_id>/entry/<entry_id>/edit_history", methods = ["GET","POST"])
def view_edit_history(blog_id,entry_id):
    if 'user' in session:
        print(entries.read_entries_h(blog_id, entry_id))
        return render_template("edit_history.html",
                        entries = entries.read_entries_h(blog_id, entry_id),
                        userid = session.get('userid')
                        )
    else:
        return redirect(url_for("login"))

@app.route("/blog/<blog_id>/entry/<entry_id>/edit", methods = ["GET","POST"])
def edit_entry(blog_id,entry_id):
    print("YOOOO")
    print (request.args)
    print(request.args.get('content'))
    if 'user' in session:
        if(session.get('user') == acc.get_username(blogs.get_userid(blog_id))):
            if(request.method == "GET"):
                content = ""
                for line in request.args.get('content'):
                    content += line
                return render_template("edit_entry.html",
                                userid = session.get('userid'),
                                content = content[2:-2],
                                blog_id = blog_id,
                                entry_id = entry_id
                                )
            elif(request.method == "POST"):
                entries.edit_entry(blog_id, entry_id, request.form['entry_content'])
                flash("Successfully edited entry")
                return redirect(url_for("view_blog", blog_id = blog_id))
        else:
            flash("Please do not try to edit other people's entries!")
            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
	app.debug = True
	app.run()

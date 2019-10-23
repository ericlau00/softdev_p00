# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os
import utl

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
        return render_template(
            "home.html",
            title= "Home"
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
        if(request.form['username'] != username): ##if request.form['username'] is not in the database
            flash("Username doesn't exist")
            return redirect(url_for("login"))
        elif(request.form['password'] != password): ##if request.form['password'] does not match password of username 
            flash("Password does not match up with username")
            return redirect(url_for("login"))
        else:
            session['user'] = request.form['username']
            flash("You have successfully logged in!")
            return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template(
            "register.html",
            title= "Register"
            )
    if(request.method == "POST"):
        ## if username is already in the database,
            # flash username take
            #return render_template("register.html")
        if request.form['password'] != request.form['confirmpassword']:
            flash("Passwords do not match")
            return render_template("register.html")
        else:
            # add account information to the database 
            session['user'] = request.form['username']
            return redirect(url_for("home"))


@app.route("/logout", methods = ["GET","POST"])
def logout():
        # remove the username from te session if it's there
        session.pop('user', None)
        flash('You were successfully logged out!')
        return redirect(url_for('login'))
        
if __name__ == "__main__":
	app.debug = True
	app.run()

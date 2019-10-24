# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os
from utl import acc

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
        if(utl.verify_acc(request.form['username'],request.form['password'])):
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
        elif (acc.push_acc(request.form['username'],request.form['password'])):
            return redirect(url_for("login"))
        else:
            flash("Username already exists")
            return render_template("register.html")


@app.route("/logout", methods = ["GET","POST"])
def logout():
        # remove the username from te session if it's there
        session.pop('user', None)
        flash('You were successfully logged out!')
        return redirect(url_for('login'))

if __name__ == "__main__":
	app.debug = True
	app.run()

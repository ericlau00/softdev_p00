# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = "user"
password = "password"

@app.route("/", methods=["GET"])
def root():
    if not 'login' in session:
        session['login'] = False
    if 'user' in session and session['login']:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

@app.route("/home", methods=["GET"])
def home():
    if not 'login' in session:
        session['login'] = False
    if 'user' in session and session['login']:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "GET"):
        return render_template("login.html")
    elif(request.method == "POST"):
        if(request.form['username'] != username or request.form['password'] != password):
            session['login'] = False
            flash("Failed login!")
            return redirect(url_for("login"))
        else:
            session['login'] = True
            session['user'] = request.form['username']
            flash("You have successfully logged in!")
            return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    return "register"

if __name__ == "__main__":
	app.debug = True
	app.run()

#SeQueL
#SoftDev1 pd1
#p00

from flask import Flask, request, session, render_template, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = "user"
password = "password"

@app.route("/", methods=["GET"])
def root():
    if not 'login' in session:
        session['login'] = False 
    if(sessions['login']):
        return redirect(url_for("home"))
    else:
        redirect(url_for("login"))

@app.route("/home", methods=["GET"])
def home():
    return render_template(
        "home.html"
    )

@app.route("login", methods=["GET,POST"])
def login():
    if(request.method == "POST"):
        return "this is a post"
    elif(request.method == "GET"):
        return "this is a get"

#Team SeQueL - Joseph Lee, Eric "Morty" Lau, and Yevgeniy Gorbachev 
#SoftDev1 pd1
#P0 -- Da Art of Storytellin'
#2019-10-28

from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

@app.route("/")
def root():
    return render_template(
        "index.html"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
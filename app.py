#SeQueL
#SoftDev1 pd1
#p00

from flask import Flask, request, session, render_template, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

#Handles account creation and usage

import sqlite3
from hashlib import md5

#checks account credentials
def check_creds(un, pw):
    print(md5(pw))

check_creds("","input pw")
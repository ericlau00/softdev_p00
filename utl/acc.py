#Handles account creation and usage

import sqlite3
from hashlib import md5
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('CREATE TABLE IF NOT EXISTS users (userid INTEGER PRIMARY KEY, username TEXT, password TEXT);')
    db.commit()

#checks account credentials
def verify_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('SELECT username, password FROM users WHERE username=?', (un,)) # find userinfo
        userinfo = [item for item in userinfo][0] # take first entry (should be at most one anyway)
        return userinfo[1] == hpw # check password hashes
    except IndexError as error: # no such username
        print(error)
        return False
    
def create_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        db.execute('INSERT INTO users VALUES (?,?,?);', (__count(), un, hpw)) # next index for userid
        db.commit()
        return True
    except sqlite3.Error as error: #uniqueness error
        print(error)
        return False
    
def __hash(txt):
    hpw = md5()
    hpw.update(txt.encode('UTF-8'))
    return hpw.hexdigest()

def __count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('SELECT count(*) FROM users;')
    return [num for num in count][0][0]
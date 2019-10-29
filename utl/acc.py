import sqlite3
from hashlib import md5
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS users (
                    userid INTEGER PRIMARY KEY,
                    username TEXT UNQIUE,
                    password TEXT
                    );''')
    db.commit()

#checks account credentials
def verify_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('SELECT password FROM users WHERE username=?;',(un,)) # find userinfo
        userinfo = [item for item in userinfo][0] # take first entry (should be at most one anyway)
        if userinfo[0] == hpw:
            return True # if credentials are good, return the userid
        else:
            return False
    except IndexError as error: # no such username, probably
        print(error)
        return False

#gets the userid that matches the username 
def get_userid(un):
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('SELECT userid FROM users WHERE username=?;',(un,))
        return [item for item in userinfo][0][0]
    except IndexError as error:
        print(error)

#if the username is unique, then insert the username and a hashed password with an incremented id.
def create_acc(un, pw):
    hpw = __hash(pw)
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('INSERT INTO users VALUES (?,?,?);', (__count(), un, hpw)) # next index for userid
        db.commit()
        return True
    except sqlite3.Error as error: # uniqueness error, probably
        print(error)
        return False

# update the username or password given that the username is unique
def edit_acc(userid, new_un='', new_pw=''):
    db = sqlite3.connect(__dbfile__)
    try:
        if new_un != '':
            db.execute('UPDATE users SET username=? WHERE userid=?;',(new_un, userid))
        if new_pw != '':
            hpw = __hash(new_pw)
            db.execute('UPDATE users SET password=? WHERE userid=?;',(hpw, userid))
        db.commit()
        return True
    except sqlite3.Error as error:
        print(error)
        return False

#given an id, return the username that matches 
def get_username(userid):
    db = sqlite3.connect(__dbfile__)
    try:
        query = db.execute(
            '''
            SELECT users.username
            FROM users
            WHERE users.userid = ?
            ''', (userid,)
            )
        return [data for data in query][0][0]
    except sqlite3.Error as error:
        print(error)
        return False

#hash the password using the md5 algorithm 
def __hash(txt):
    hpw = md5()
    hpw.update(txt.encode('UTF-8'))
    return hpw.hexdigest()

#get the count of the number of users 
def __count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('SELECT count(*) FROM users;')
    return [num for num in count][0][0]

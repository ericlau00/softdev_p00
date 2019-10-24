#Handles account creation and usage

import sqlite3
from hashlib import md5

__dbfile__ = '../data/sitedata.db'

#checks account credentials
def verify_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('select username, password from users where username=?', (un,)) # find userinfo
        userinfo = [item for item in userinfo][0] # take first entry (should be at most one anyway)
        return userinfo[1] == hpw # check password hashes
    except IndexError as error: # no such username
        print(error)
        return False
    


def create_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        db.execute('insert into users values (?,?,?);', (__count(), un, hpw)) # next index for userid
        db.commit()
        return True
    except sqlite3.Error as error: #uniqueness error
        return False
    
def __hash(txt):
    hpw = md5()
    hpw.update(txt.encode('UTF-8'))
    return hpw.hexdigest()

def __count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('select count(*) from users;')
    return [num for num in count][0][0]

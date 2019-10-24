#Handles account creation and usage

import sqlite3
from hashlib import md5

__dbfile__ = '../data/sitedata.db'

#checks account credentials
def verify_acc(un, pw):
    hpw = hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('select username, password from users where username = ?', (un,))
        status = [item for item in userinfo][0][1] == hpw
        print(userinfo)
        print(status)
        return status
    except sqlite3.Error as error:
        print(error)
        return False
    


def create_acc(un, pw):
    hpw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        db.execute('insert into users values (?,?,?);', (__count(), un, hpw))
        db.commit()
        return True
    except sqlite3.Error as error:
        return False
    
def __hash(txt):
    hpw = md5()
    hpw.update(txt.encode('UTF-8'))
    return hpw.hexdigest()

def __count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('select count(*) from users;')
    return [num for num in count][0][0]

#Handles account creation and usage

import sqlite3
from hashlib import md5

__dbfile__ = '../data/sitedata.db'

#checks account credentials
def verify_acc(un, pw):
    hpw = pw
    # hpw = hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        userinfo = db.execute('select username, password from users where username = ?', (un,))
    except sqlite3.Error as error:
        print(error)
        return False
    status = [item for item in userinfo][0][1] == hpw
    print(status)
    return status
    


def create_acc(un, pw):
    # pw = __hash(pw)
    try:
        db = sqlite3.connect(__dbfile__)
        db.execute('insert into users values (?,?,?);', (__count(), un, pw))
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
    db.close()
    return [num for num in count][0][0]

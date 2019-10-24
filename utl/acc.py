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
        db.close()
    except sqlite3.Error as error:
        print(error)
        return False
    return [item for item in userinfo][0][1] == hpw
    


def __push_acc(un, pw):
    uid = 0
    with open('counters','w') as cfile:
        counts = [int(c) for c in '\n'.split(cfile.read())]
        try:
            db = sqlite3.connect(__dbfile__)
            db.execute('insert into users values (?,?,?);', (counts[0] + 1, un, pw))
        except sqlite3.Error as error:
            return False
        counts[0] += 1
        cfile.write(str(counts[0]) + '\n' + str(counts[1]))
def __hash(txt):
    hpw = md5()
    hpw.update(txt.encode('UTF-8'))
    return hpw.hexdigest()
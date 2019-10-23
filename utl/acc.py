#Handles account creation and usage

import sqlite3
from hashlib import md5

__dbfile__ = '../data/sitedata.db'
db = sqlite3.connect(__dbfile__)

#checks account credentials
def verify_acc(un, pw):
    hpw = md5()
    hpw.update(pw.encode('UTF-8'))
    hpw = hpw.hexdigest()
    try:
        userinfo = db.execute('select username, password from users where username= ?', (un,))
    except sqlite3.Error as error:
        print(error)
        return False
    return [item for item in userinfo][0][1] == hpw
    


def push_acc(un, pw):
    uid = 0
    with open('counters','w') as cfile:
        counts = [int(c) for c in '\n'.split(cfile.read())]
        counts[0] += 1
        uid = counts[0]
        insert(uid, un, pw)
        cfile.write(str(counts[0]) + '\n' + str(counts[1]))

def insert(id, un, pw):
    db.execute('insert into users values (?,?,?);', (id, un, pw))


db.commit()
db.close()
import sqlite3
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def create_blog(userid, title):
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('insert into blogs values (userid, blogid, title) values (?,?,?);', (userid, __count(), title))
        return True
    except sqlite3.Error as error:
        return False


def describe(title):
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('select userid, username, title from blogs where')


def __count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('select count(*) from blogs;')
    return [num for num in count][0][0]

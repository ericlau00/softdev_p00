import sqlite3
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def create_blog(userid, title):
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('insert into blogs values (?,?,?);', (userid, count(), title))
        db.commit()
        return True
    except sqlite3.Error as error:
        print(error)
        return False


def describe(id):
    db = sqlite3.connect(__dbfile__)
    try:
        desc = db.execute('select users.username, users.userid, blogs.title from blogs inner join users on blogs.userid = users.userid where blogs.blogid = ?', (id,))
        return [data for data in desc][0]
    except sqlite3.Error as error:
        print(error)
        return False

def count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('select count(*) from blogs;')
    return [num for num in count][0][0]

# create_blog(0, "eric's blogs")
# describe(1)
import sqlite3
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('CREATE TABLE IF NOT EXISTS blogs (userid INTEGER, blogid PRIMARY KEY, title TEXT UNIQUE);')
    db.commit()

def create_blog(userid, title):
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('INSERT INTO blogs VALUES (?,?,?);', (userid, count(), title))
        db.commit()
        return True
    except sqlite3.Error as error:
        print(error)
        return False

def describe(blogid):
    db = sqlite3.connect(__dbfile__)
    try:
        desc = db.execute(
            '''
            SELECT users.username, users.userid, blogs.title 
            FROM blogs 
            INNER JOIN users 
            ON blogs.userid = users.userid 
            WHERE blogs.blogid = ?
            ''', (blogid,)
            )
        return [data for data in desc][0]
    except sqlite3.Error as error:
        print(error)
        return False

# def read_entries(blogid):


def count():
    db = sqlite3.connect(__dbfile__)
    count = db.execute('SELECT count(*) FROM blogs;')
    return [num for num in count][0][0]

create_blog(2, "hog")
# describe(1)
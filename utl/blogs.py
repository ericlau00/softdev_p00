import sqlite3
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS blogs (
                    userid INTEGER,
                    blogid PRIMARY KEY,
                    title TEXT UNIQUE);
                ''')
    db.commit()

def create_blog(userid, title):
    db = sqlite3.connect(__dbfile__)
    try:
        db.execute('INSERT INTO blogs VALUES (?,?,?);', (userid, count(), title))
        db.commit()
        return True
    except sqlite3.Error as error: # uniqueness probably
        print(error)
        return False

def delete_blog(blogid):
    db = sqlite3.connect(__dbfile__)

def describe(blogid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute(
            '''
            SELECT blogs.blogid, blogs.title, users.userid, users.username
            FROM blogs
            INNER JOIN users
            ON blogs.userid = users.userid
            WHERE blogs.blogid = ?
            ''', (blogid,)
            )
    try:
        return [data for data in query][0]
    except IndexError as error:
        return False

def read_entries(blogid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('''
                    SELECT entryid, versionid, timestamp, content FROM entries
                    WHERE blogid=?
                    ORDER BY entryid DESC
                    ''', (blogid,))
    elist = [item for item in query]
    for i in range(len(elist)):
        elist[i] = {
            'entryid':elist[i][0],
            'versionid':elist[i][1],
            'timestamp':elist[i][2],
            'content':list(elist[i])[3].split("\n"),
        }
    return elist

def get_user_blogs(userid):
    db = sqlite3.connect(__dbfile__)
    try:
        query = db.execute(
            '''
            SELECT blogs.blogid, blogs.title
            FROM blogs
            WHERE blogs.userid = ?
            ''', (userid,)
            )
        return [data for data in query]
    except sqlite3.Error as error:
        print(error)
        return False

def get_userid(blogid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute(
            '''
            SELECT blogs.userid
            FROM blogs
            WHERE blogs.blogid = ?
            ''', (blogid,)
            )
    try:
        return [data for data in query][0][0]
    except IndexError as error:
        return False
##SUPPLEMENTARY
def count():
    db = sqlite3.connect(__dbfile__)
    query = db.execute('SELECT count(*) FROM blogs;')
    return [num for num in query][0][0]

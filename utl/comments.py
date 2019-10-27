import sqlite3
import os
import datetime

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS comments(
                    blogid INTEGER,
                    entryid INTEGER,
                    commentid INTEGER,
                    userid INTEGER,
                    timestamp TEXT,
                    content TEXT);''')
    db.commit()

def create_comment(blogid, entryid, userid, content):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('SELECT count(*) FROM comments WHERE blogid=? AND entryid=?;',(blogid, entryid))
    count = [item for item in query][0][0]
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    db.execute('INSERT INTO comments VALUES (?,?,?,?,?,?)', (blogid, entryid, count, userid, time, content))
    db.commit()
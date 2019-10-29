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

#creates a comment with timestamp of when it was created
def create_comment(blogid, entryid, userid, content):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('SELECT commentid FROM comments WHERE blogid=? AND entryid=?;',(blogid, entryid))
    ids = [item[0] for item in query]
    ids.append(0)
    count = max(ids)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    db.execute('INSERT INTO comments VALUES (?,?,?,?,?,?)', (blogid, entryid, count, userid, time, content))
    db.commit()

#deletes a comment linked to blog and entry
def delete_comment(blogid, entryid, commentid):
    db = sqlite3.connect(__dbfile__)
    db.execute('DELETE FROM comments WHERE blogid=? AND entryid=? AND commentid=?;',(blogid, entryid, commentid))
    db.commit()

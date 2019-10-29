import sqlite3
import os
import datetime
from utl import acc

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS entries (
                    blogid INTEGER,
                    entryid INTEGER,
                    versionid INTEGER,
                    timestamp INTEGER,
                    title TEXT,
                    content TEXT);''')
    db.commit()

#this is an archive of all entries to be able to view entry history 
def init_arc():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS entries_arc (
                    blogid INTEGER,
                    entryid INTEGER,
                    versionid INTEGER,
                    timestamp INTEGER,
                    title TEXT,
                    content TEXT);''')
    db.commit()

def create_entry(blogid, title, content):
    db = sqlite3.connect(__dbfile__)

    query = db.execute('SELECT count(*) FROM entries WHERE blogid=?;',(blogid,))
    count = [item for item in query][0][0]
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    #count of entries starts at 1
    #version starts at 0
    db.execute('INSERT INTO entries VALUES (?,?,?,?,?,?)',(blogid, count + 1, 0, time, title, content))
    db.execute('INSERT INTO entries_arc VALUES (?,?,?,?,?,?)',(blogid, count + 1, 0, time, title, content))
    db.commit()

def read_entry(blogid, entryid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('SELECT title, content FROM entries WHERE blogid=? AND entryid=?', (blogid, entryid))

    query = [item for item in query][0]
    entry = {
        'title': query[0],
        #splits on new line to be able to show new lines on html frontend
        'content': query[1].split("\n")
    }
    return entry

#updates the current entry in entries table 
#makes a new version of the entry in the entries_arc table
def edit_entry(blogid, entryid, title, content):
    db = sqlite3.connect(__dbfile__)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    query = db.execute('SELECT versionid FROM entries WHERE blogid=? AND entryid=?;',(blogid, entryid))
    current = [item for item in query][0][0]

    db.execute('UPDATE entries SET versionid=?, content=?, title=? WHERE blogid=? AND entryid=?;', (current, content, title, blogid,entryid))
    db.execute('INSERT INTO entries_arc VALUES (?,?,?,?,?,?);', (blogid, entryid, current, time, title, content))
    db.commit()

#deletes entry linked to blog and entry id 
def delete_entry(blogid, entryid):
    db = sqlite3.connect(__dbfile__)
    db.execute('DELETE FROM entries WHERE blogid=? AND entryid=?;', (blogid, entryid))
    db.execute('DELETE FROM entries_arc WHERE blogid=? AND entryid=?;', (blogid, entryid))
    db.commit()

#returns all of the previous versions of an entry 
def read_entries_h(blogid, entryid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('''
            SELECT versionid, timestamp, title, content
            FROM entries_arc WHERE blogid=? AND entryid=?
            ORDER BY versionid DESC''',(blogid, entryid))
    hist = [item for item in query]
    for i in range(len(hist)):
        hist[i] = {
            'versionid':hist[i][0],
            'timestamp':hist[i][1],
            'title':hist[i][2],
            'content':hist[i][3].split("\n"),
        }
    return hist

#get all of the comments that are linked to an entry
def read_comments(blogid, entryid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('''
            SELECT comments.userid, comments.timestamp, comments.content, comments.commentid
            FROM comments WHERE comments.blogid=? AND comments.entryid=?
            ORDER BY commentid DESC''',(blogid, entryid))
    comments = [item for item in query]
    for i in range(len(comments)):
        comments[i] = {
            'userid':comments[i][0],
            'username':acc.get_username(comments[i][0]),
            'timestamp':comments[i][1],
            'content':comments[i][2].split("\n"),
            'commentid':comments[i][3]
        }
    for item in comments:
        print(item)
    return comments

#get the count of comments 
def count_comments(blogid, entryid):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('SELECT count(*) FROM comments WHERE blogid=? AND entryid=?',(blogid, entryid))
    return [item for item in query][0][0]
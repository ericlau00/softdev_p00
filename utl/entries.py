import sqlite3
import os
import datetime


__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def init():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS entries (
                    blogid INTEGER, 
                    entryid INTEGER, 
                    versionid INTEGER, 
                    timestamp INTEGER, 
                    content TEXT);''')
    db.commit()

def init_arc():
    db = sqlite3.connect(__dbfile__)
    db.execute('''CREATE TABLE IF NOT EXISTS entries_arc (
                    blogid INTEGER, 
                    entryid INTEGER, 
                    versionid INTEGER, 
                    timestamp INTEGER, 
                    content TEXT);''')
    db.commit()

def create_entry(userid, blogid, content):
    db = sqlite3.connect(__dbfile__)

    count = db.execute('SELECT count(*) FROM entries WHERE blogid=?;',(blogid,))
    count = [item for item in count][0][0]
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    db.execute('INSERT INTO entries VALUES (?,?,?,?,?)',(blogid, count, 0, time, content))
    db.execute('INSERT INTO entries_arc VALUES (?,?,?,?,?)',(blogid, count, 0, time, content))
    db.commit()

def edit_entry(blogid, entryid, content):
    db = sqlite3.connect(__dbfile__)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    current = [item for item in db.execute('SELECT versionid FROM entries WHERE blogid=? AND entryid=?',(blogid, entryid))][0][0]

    db.execute('UPDATE entries SET versionid=?, content=?', (current + 1, content))
    db.execute('INSERT INTO entries_arc VALUES (?,?,?,?,?)', (blogid, entryid, current + 1, time, content))
    db.commit()

create_entry(1, 0, "This is a test entry for eric's blog")
edit_entry(0, 0, "This is the edited test entry for eric's blog")
import sqlite3
import os

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



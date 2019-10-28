import sqlite3
import os

__dbfile__ = os.path.dirname(os.path.abspath(__file__)) + '/../data/sitedata.db'

def search(keyword):
    db = sqlite3.connect(__dbfile__)
    query = db.execute('''
                        SELECT blogs.blogid, blogs.title, users.userid, users.username 
                        FROM blogs INNER JOIN users ON blogs.userid = users.userid
                        WHERE blogs.title LIKE ?;''',(f'%{keyword}%',))
    results = [item for item in query]
    for i in range(len(results)):
        results[i] = {
            'blogid':results[i][0],
            'title':results[i][1],
            'userid':results[i][2],
            'username':results[i][3],
        }
    return results
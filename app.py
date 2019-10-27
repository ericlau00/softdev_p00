# Team SeQueL - Joseph Lee, Yevgeniy Gorbachev, Eric Lau
# SoftDev1 pd1
# P0 The Art of Storytellin'
# 2019-10-28

from flask import Flask, request, redirect, session, render_template, url_for, flash
import os
from utl import acc, blogs, comments, entries, search

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET'])
def root():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/home', methods=['GET'])
def home():
    if 'user' in session:
        count = blogs.count()
        info = []
        for i in range(count):
            info.append(blogs.describe(i))
        return render_template(
            'home.html',
            blogs = info,
            userid = session.get('userid')
            )
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if(request.method == 'GET'):
        if 'user' in session:
            return redirect(url_for('home'))
        else:
            return render_template(
                'login.html',
                )
    elif(request.method == 'POST'):
        session['userid'] = acc.verify_acc(request.form['username'],request.form['password'])
        if session.get('userid') != False:
            session['user'] = request.form['username']
            flash('You have successfully logged in!')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method == 'GET'):
        return render_template(
            'register.html',
            )
    if(request.method == 'POST'):
        if request.form['password'] != request.form['confirmpassword']:
            flash('Passwords do not match')
            return render_template('register.html')
        elif (acc.create_acc(request.form['username'],request.form['password'])):
            return redirect(url_for('login'))
        else:
            flash('Username already exists')
            return render_template('register.html')

@app.route('/logout', methods = ['GET','POST'])
def logout():
        # remove the username from the session if it's there
        session.pop('user', None)
        flash('You were successfully logged out!')
        return redirect(url_for('login'))

@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    if 'user' in session:
        if(request.method == 'GET'):
            return render_template('settings.html',
                                    userid = session.get('userid'))
        elif(request.method == 'POST'):
            if request.form['password'] != request.form['confirmpassword']:
                flash('Passwords do not match')
                return render_template('settings.html')
            elif (acc.edit_acc(session.get('userid'),request.form['username'],request.form['password'])):
                flash('Successfully reset credentials')
                return redirect(url_for('home'))
            else:
                flash('Username already exists')
                return render_template('settings.html')
    else:
        return redirect(url_for('login'))

@app.route('/search', methods = ['GET', 'POST'])
def lookup():
    if 'user' in session:
        if(request.method == 'GET'):
            return render_template('search.html',
                                    userid = session.get('userid'),
                                    query = '',
                                    blogs = [])
        if(request.method == 'POST'):
            return render_template('search.html',
                                    userid = session.get('userid'),
                                    blogs = search.search(request.form['search_query']),
                                    query = request.form['search_query'])
    else:
        return redirect(url_for('login'))

@app.route('/profile/<userid>', methods=['GET'])
def profile(userid):
    username = acc.get_username(userid)
    if 'user' in session:
        return render_template('profile.html',
                                title = username,
                                username = username,
                                user_blogs = blogs.get_user_blogs(userid),
                                is_owner = (str(session.get('userid')) == userid),
                                userid = session.get('userid')
                                )
    else:
        return redirect(url_for('login'))

@app.route('/profile/create_blog', methods =['GET','POST'])
def create_blog():
    if 'user' in session:
        if(request.method == 'GET'):
            return render_template('create_blog.html',
                                    userid = session.get('userid'))
        if(request.method == 'POST'):
            if request.form['blog_title'] == '' or request.form['blog_title'].isspace():
                flash('please input a blog title')
                return redirect(url_for('create_blog'))
            blogs.create_blog(session.get('userid'), request.form['blog_title'])
            flash('You have successfully created a blog!')
            return redirect(url_for('profile', userid = session.get('userid')))
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>', methods = ['GET','POST'])
def view_blog(blogid):
    if 'user' in session:
        #print(blogs.read_entries(blogid)[0]['content'])
        return render_template('blog.html',
            blogid = blogid,
            description = blogs.describe(blogid),
            entries = blogs.read_entries(blogid),
            is_owner = (session.get('userid') == blogs.get_userid(blogid)),
            userid = session.get('userid')
            )
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/create_entry', methods = ['GET','POST'])
def create_entry(blogid):
    if 'user' in session:
        if(session.get('userid') == blogs.get_userid(blogid)):
            if(request.method == 'GET'):
                return render_template('create_entry.html',
                                        blogid = blogid,
                                        userid = session.get('userid')
                                        )
            elif(request.method == 'POST'):
                if request.form['entry_title'] == '' or request.form['entry_title'].isspace() or request.form['entry_content'] == '' or request.form['entry_content'].isspace():
                    flash('please input some text')
                    return render_template('create_entry.html',
                                            blogid=blogid,
                                            userid = session.get('userid')
                                            )
                else:
                    entries.create_entry(blogid,
                                        request.form['entry_title'],
                                        request.form['entry_content']
                                        )
                    flash('You have successfully created an entry!')
                    return redirect(url_for('view_blog', blogid = blogid))
        else:
            flash('Please do not try to create entries for other people\'s blogs!')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/<entryid>/view', methods = ['GET','POST'])
def view_entry(blogid,entryid):
    if 'user' in session:
        if(request.method == 'GET'):
            return render_template('entry.html',
                                    blogid = blogid,
                                    entryid = entryid,
                                    description = blogs.describe(blogid),
                                    entry = entries.read_entry(blogid, entryid),
                                    is_owner = session.get('userid') == blogs.get_userid(blogid),
                                    userid = session.get('userid'),
                                    comments = entries.read_comments(blogid,entryid)
                                    )
        elif(request.method == 'POST'):
            comments.create_comment(blogid,
                                    entryid,
                                    session.get('userid'),
                                    request.form['comment_content'])
            flash('successfully commented')
            return redirect(url_for('view_entry', blogid = blogid, entryid = entryid))
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/<entryid>/edit_history', methods = ['GET','POST'])
def view_edit_history(blogid,entryid):
    if 'user' in session:
        return render_template('edit_history.html',
                        entries = entries.read_entries_h(blogid, entryid),
                        userid = session.get('userid')
                        )
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/<entryid>/edit', methods = ['GET','POST'])
def edit_entry(blogid,entryid):
    if 'user' in session:
        entry = entries.read_entry(blogid, entryid)
        for line in range(len(entry['content'])):
            entry['content'][line] = entry['content'][line].replace('\r','')
        if(session.get('userid') == blogs.get_userid(blogid)):
            if(request.method == 'GET'):
                return render_template('edit_entry.html',
                                userid = session.get('userid'),
                                entry = entry,
                                blogid = blogid,
                                entryid = entryid
                                )
            elif(request.method == 'POST'):
                entries.edit_entry(blogid, entryid, request.form['title'], request.form['entry_content'])
                flash('Successfully edited entry')
                return redirect(url_for('view_entry', blogid = blogid, entryid = entryid))
        else:
            flash('Please do not try to edit other people\'s entries!')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/<entryid>/delete', methods = ['GET','POST'])
def delete_entry(blogid,entryid):
    if 'user' in session:
        if(session.get('userid') == blogs.get_userid(blogid)):
            entries.delete_entry(blogid, entryid)
            flash('Successfully deleted entry')
            return redirect(url_for('view_blog', blogid = blogid))
        else:
            flash('Please do not try to delete other people\'s entries!')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/blog/<blogid>/<entryid>/<commentid>/<userid>/delete', methods = ['GET','POST'])
def delete_comment(blogid,entryid,commentid,userid):
    if 'user' in session:
        if(session.get('userid') == userid):
            comments.delete_comment(blogid,entryid,commentid)
            flash('Successfully deleted comment')
            return redirect(url_for('view_entry', blogid = blogid, entryid = entryid))
        else:
            flash('Please do not try to delete other people\'s comments!')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    blogs.init()
    acc.init()
    entries.init()
    entries.init_arc()
    comments.init()
    app.debug = True
    app.run()

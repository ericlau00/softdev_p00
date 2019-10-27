# tumblr the SeQueL by SeQueL

## Roster 
- **Eric Lau** (Project Managar)
    - Help out with frontend and backend tasks when applicable
    - Team management 
    - Devlog and update design doc
- **Yevgeniy Gorbachev**
    - Everything database related
        - Fetching blog entries, list of blogs, etc.
        - Adding users, blogs, entries, comments to database
- **Joseph Lee**
    - App routing and redirecting
    - Implementing front-end

## Instructions
**Assuming python3 and pip are already installed**
### Virtual Environment 
- To prevent conflicts with globally installed packages, it is recommended to run everything below in a virtual environment. 

Set up a virtual environment by running the following in your terminal:
```
python -m venv hero 
# replace hero with anything you want 
# If the above does not work, run with python3 (this may be the case if a version of python2 is also installed)
```

To enter your virtual environment, run the following:
```
. hero/bin/activate
```

To exit your virtual environment, run the following:
```
deactivate
```


### Dependencies 
- **Flask**
    - Install by running `pip install flask` in your terminal
        - If the above does not work, run `pip3 install flask` (this may be the case if a version of python2 is also installed)
    
### Imported Modules (all are included within the Python Standard Library)
- [os](https://docs.python.org/3/library/os.html)
    - module helps with reading or writing other files in the computer
    - our file structure of utl and data created a situation such that referring to the database in utl required changing directories and we decided it would be better to have an absolute path
    - we create an absolute path to our database by using os.path
- [hashlib](https://docs.python.org/3/library/hashlib.html)
    - module implements various ways to hash messages 
    - we think that it is more secure to store a hashed password in our database than to store the password itself
    - when registering an account, the user-inputted password is hashed with the md5 algorithm and stored in the users table 
    - when logging in, the user-inputted password is hashed with the md5 algorithm and checked against the password in the database 
- [datetime](https://docs.python.org/3/library/datetime.html)
    - module supports manipulation of dates and times
    - we want to be able to show when comments and entries are created
    - when inserting comments and entries, we convert dates to integers and convert back to strings to display
    
### How to run
- Run `python app.py` in the directory
    - If the above does not work, run `python3 app.py` (this may be the case if a version of python2 is also installed)
- Open your browser to localhost:5000

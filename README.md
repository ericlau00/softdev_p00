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
### Dependencies 
- **Flask**
    - Install by running `pip install flask` in your terminal

### Imported Modules (All are included within the Python Standard Library)
- [os](https://docs.python.org/3/library/os.html)
    - module helps with reading or writing other files in the computer
    - our file structure of utl and data created a situation such that referring to the database in utl required changing directories and we decided it would be better to have an absolute path
    - we create an absolute path to our database by using os.path
- [hashlib](https://docs.python.org/3/library/hashlib.html)
    - module implements various ways to hash messages 
    - we think that it is more secure to store a hashed password in our database than to store the password itself
    - when registering an account, the user-inputted password is hashed with the md5 algorithm and stored in the users table 
    - when logging in, the user-inputted password is hashed with the md5 algorithm and checked against the password in the database 
### How to run
- Run `python3 app.py` in the directory
- Open your browser to localhost:5000

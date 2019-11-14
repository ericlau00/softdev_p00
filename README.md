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

---
# P #00: Da Art of Storytellin'

Due **M 2019-10-28**, 08:00, EST.

*Imagine one of these scenarios*:

<u> Scenario One </u>: Your team has been contracted to create a 
**collaborative storytelling game/website**.

- Users will have to register to use the site.
- Logged-in users can either start a new story or add to an existing story.
- When adding to a story,
    - Users are shown only the latest update to the story, not the whole thing.
    - A user can then add some amount of text to the story.
- Once a user has added to a story, they cannot add to it again.
- When creating a new story,
    - Users get to start with any amount of text and give the story a title.
    - Logged in users will be able to read any story they have contributed to on their homepage (the landing page after login).

<u>Scenario Two</u>: Your team has been contracted to create a **we*b log* hosting site**.

- Users will have to register to use the site.
- Logged-in users will be able to
    - Create a new blog
    - Update their blog by adding a new entry
    - View and edit their own past entries
    - View the blogs of other users

Your “software solution” will incorporate a few distinct components, so it is imperative that your team develop a design and agree upon roles before you move to implementation.

**There will be no CSS.**

You will need a DEVLOG for this project.

- The purpose of the devlog is to allow any group member at any time to see the current state of the project.
- PM will make sure devlog is being maintained, but *will not* make all entries.
- The devlog should be a plain text file, stored in the specified location.
- When any team member stops working and pushes changes to github, they should update the devlog explaining what changes have been made. Include errors/bugs discovered (or created).
- Separate devlog entries with a newline.
- Most recent entry at the bottom.
- Each entry should begin with the following format: <br>
`firstL -- TIMESTAMP\n`
*e.g.*:
`topherM -- 1999-12-31 23:59`

## Task the First: The Plan . . .  

Due **M 2019-10-21**, 08:00, EST.

**Create a design document** for your project.

- Include these, as well as any necessary supporting documentation:
    - component map
    - site map
    - database layout diagram
- Divide the tasks among your group members. (Assign roles.)
- One role must be "Project Manager," who...
    - Has not served as PM before.
    - Makes sure the group is consistently moving together.
    - Handles (minor) coding tasks as necessary.
    - Makes certain the design document is coherent and that the group is adhering to agreed-upon design.
    - Stays abreast of any changes made to the design, and is responsible for creating
        - revised version(s) of design doc
        - entries in devlog addressing necessity for mid-development modifications
- There will be a summary document at the end of the project created by the group; the project manager will have certain duties pertaining to that document as well.
- PRELIMINARY DELIVERABLES:
    - PDF named `design.pdf` in appropriate location.
    - hardcopy x3
- Submodule linking notes:
Link your submodule in [upgraded-octo-waffle](https://www.google.com/url?q=https://github.com/stuy-softdev/upgraded-octo-waffle&sa=D&ust=1573706303434000) repository. (`bit.ly/p0-1920`)
- Name your submodule link as follows:<br>
`name_of_team__lastaF-lastbF`<br>
(*e.g.*, `gangstarr__dyrlandweaverJ-mykolykT`)

## Task the Second: "Wait what, we can't use any CSS?!?! How will we write our deep learning rocket engine? Ack, the horror!" . . . 

Due **T 2019-10-22**, 08:00, EST.

- Revise your design doc in response to feedback given from reviewing teams.
- Create a devlog entry summarizing your changes.
- Gather ye round the [virtual] campfire, and over [virtual] hot chocolate, read these with your team:
    - sqlitetutorial.net/sqlite-join/
    - sqlitetutorial.net/sqlite-inner-join/
    - sqlitetutorial.net/sqlite-left-join/
    - sqlitetutorial.net/sqlite-cross-join/
- Via a devlog entry, summarize each of these operations and how it may apply to your current project.
- Gather ye round the [virtual] campfire, and over [virtual] hot chocolate, read [this](https://www.google.com/url?q=https://www.stilldrinking.org/programming-sucks&sa=D&ust=1573706303436000) with your team.
- Via a devlog entry, respond to said reading and note 2-3 concrete actions your team will take or procedures/protocols you will observe to make more awesome.

## Task the Toid: Point Their-Up-Goer-Skyward
Due **F 2019-10-25**, 08:00, EST.

Your README.md should include clear instructions on how to run your project.

- Assume your audience is cloning your repo and running from localhost.
- List dependencies (pip installs, at most, for this project), as well as how to install/procure them if necessary.
- For any module/library/etc for which special clearance was required, include
    - Link to primary documentation
    - Succinct, clear explanation of what it does
    - Succinct, clear explanation of why you deemed it necessary
    - Clear, precise explanation of how it is used in your project
- Use appropriate formatting to denote commands, etc.

FINAL DELIVERABLES (*stay tuned for updates*):

- hardcopy:
    - final version of design doc (x1)
    - staple
- in `<reporoot>/doc/`:
    - `devlog.txt`
    - `design.pdf`
        - Latest/current version of your design document.
        - Revisions since v0 noted/explained in devlog.
in `<reporoot>/`:
    - `README.md`
        - Clearly visible at top:
            - &lt;Project Name&gt; by &lt;Team Name&gt;
            - Roster with roles

# Heroku
Link -

# Spotify Music Share
![](/src/images/logo.jpg)
It's lonely to listen by yourself, come and find a connection and share your taste to others


## About
Spotify music is a web app that allows people to find connections with other music lovers like
yourself. You can create groups and share playlists and find wonderful new connections. Don't just
vibe by yourself, let's all share some music. This app utilizes the spotify api, which allows you
to see all of your spotify data from a different location.

# Installation
To start, clone this project from this public github
    git clone git@github.com:GeorgiaState048/SpotifyMusicShare.git
## Please install these packages:
     install python3-pip
     pip3 install requests
     pip3 install python-dotenv
     pip3 install flask
     pip3 install json
     pip3 install Flask-SQLAlchemy==2.1
     pip3 install psycopg2-binary
     sudo apt install postgresql
     sudo apt install npm
     npm install axios
## Create a .env file and env.js file
    CLIENT_ID=""
    SECRET_KEY=""
    SQLALCHEMY_DATABASE_URI=""
## Run these commands to have an idea of starting the app
    npm install
    npm run build
### after you ran these commands then you can run the app
    python3 app.py
# Linting
    pylint: disable=no-member(disable this to remove error for SQL)
    pylint: disable=too-few-public-methods(models will have its own file)
    pylint: disable=unused-import (temporary)
    pylint: disable=invalid-name (temporary)
    pylint: disable=undefined-variable(conflicted with unit testing)
    pylint: disable=redefined-outer-name(conflcted with unit testing)
    pylint: disable=unused-variable(conflicted with unit testing)
    pylint: disable=no-name-in-module(module was required to unit test)
    pylint: disable=import-error(false error on the module)

## User Access
    We did not find out until later into the proejct that every user must be registered with the Spotify API project that we created in order to pull their data. The max amount of users that can be register for this project is 25. Also, the users must have premium accounts. If you would like for me to register you with this project, please send me an email with your spotify account email and the name associated with your account!

    If you do not want to do this, feel free to use the provided login credentials:
    Username: jonathanlaurent01
    Password: Monitor!013

# Creators
- Jonathan Laurent
- Daniel Nguyen
- Kevin Huynh
   

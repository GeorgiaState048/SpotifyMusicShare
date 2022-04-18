import os
import random
import flask
import json
import requests
from flask_sqlalchemy import SQLAlchemy

# things to do tomorrow
# database structure
#   what data should I tie to each user?
# Group pages
# update readMe
# that's it lol
access = []
user_id = [" "]

app = flask.Flask(__name__)
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# Point SQLAlchemy to your Heroku database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://ikycucawtdzvhv:b0cb879d7f7f858cde815c52bd175876eb87de197da2af2da8e62059a6e7f823@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d6af6pmuc9gt36"
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "this is a secret key!!!"

db = SQLAlchemy(app)
# dummy API
groups = [
    {
        "id": 1,
        "name": "Jazz Lover",
        "date_created": "5 weeks",
        "description": "For Jazz Music.",
    },
    {
        "id": 2,
        "name": "Music Recommendation",
        "date_created": "8 months",
        "description": "Group for music recommnedation. Drop your sickest beat here.",
    },
    {
        "id": 3,
        "name": "Chill lofi",
        "date_created": "1 year",
        "description": "Collection of chill Lofi music. Check us out!",
    },
    {
        "id": 4,
        "name": "Justin Beiber's Anti-Fan Club",
        "date_created": "5 years",
        "description": "'nuff said.",
    },
]
# MODEL, will put in a seperate file later
# class Group(db.Model):
#     """class for groups"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)
#     date_created = db.Column(db.String)
#     description = db.Column(db.String)
#     posted_by =  db.Column(db.String, db.ForeignKey('user.id'))


class Person(db.Model):
    """class person"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(1000), unique=False, nullable=False)


class Playlists(db.Model):
    """class for playlists"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    playlist = db.Column(db.String(150), unique=False, nullable=False)
    url = db.Column(db.String(150), unique=True, nullable=False)



db.create_all()

# routes interpret different pages of a page
# @bp.route("/")
# def index():
#     """initial html page""
#     return flask.render_template("newIndex.html")


@bp.route("/")
def index():
    """initial react page"""
    return flask.render_template("index.html")


@bp.route("/home", methods=["POST", "GET"])
def homepage():
    """homepage"""
    if flask.request.method == "POST":
        group_name = flask.request.form["Gname"]
        description = flask.request.form["group_description"]
        new_id = len(groups) + 1
        new_group = {
            "id": new_id,
            "name": group_name,
            "date_created": "just now",
            "description": description,
        }
        groups.append(new_group)
    return flask.render_template("home.html", groups=groups)


@bp.route("/group/<int:group_id>")
def group_details(group_id):
    """group details"""
    group = next((group for group in groups if group["id"] == group_id), None)


@bp.route("/get_access_token", methods=["GET", "POST"])
def get_access_token():
    """gets access token"""
    # i created a variable called access that holds the access token
    # this variable is populated as soon as the app loads
    if flask.request.method == "POST":
        info = json.loads(flask.request.data)
        access.append(info["token"])
    return access[0]


@bp.route("/user_info", methods=["GET", "POST"])
def get_user_info():
    """gets current user info"""
    user_endpoint = "https://api.spotify.com/v1/me"
    response = requests.get(
        user_endpoint,
        headers={
            "Authorization": "Bearer " + access[-1],
        },
    )
    response_json = response.json()
    user = response_json["display_name"]
    current_id = response_json["id"]
    images = response_json["images"][0]["url"]
    id_exists = Person.query.filter_by(username=current_id).all()
    if len(id_exists) >= 1:
        print("user already exists")
    else:
        new_user = Person(username=current_id, image=images)
        db.session.add(new_user)
        db.session.commit()
    return flask.jsonify(
        [
            {"Username": user},
            {"ProfilePic": images},
        ]
    )

@bp.route("/get_playlists", methods=["GET", "POST"])
def get_playlists():
    """gets spotify playlists for current user"""
    user_endpoint = "https://api.spotify.com/v1/me/playlists"
    response = requests.get(
        user_endpoint,
        headers={
            "Authorization": "Bearer " + access[-1],
        },
    )
    response_json = response.json()
    items = response_json["items"]
    playlist_names = []
    for i in items:
        playlist_name = i["name"]
        playlist_url = i["external_urls"]["spotify"]
        playlist_id = i["owner"]["id"]
        playlist_names.append((playlist_name, playlist_url))
        playlist_exists = Playlists.query.filter_by(url=playlist_url).all()
        if len(playlist_exists) >= 1:
            print("playlist already exists")
        else:
            new_playlist = Playlists(
                username=playlist_id, playlist=playlist_name, url=playlist_url
            )
            db.session.add(new_playlist)
            db.session.commit()
    return flask.jsonify(
        [
            {"PlaylistNames": playlist_names},
        ]
    )


app.register_blueprint(bp)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8000)))
# app.run()

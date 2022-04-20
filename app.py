# pylint: disable=no-member
# pylint: disable=too-few-public-methods
"""import libaries and calling others"""
import os
import json
import flask
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
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
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ikycucawtdzvhv:b0cb879d7f7f858cde815c52bd175876eb87de197da2af2da8e62059a6e7f823@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d6af6pmuc9gt36"
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

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

class Group(db.Model):
    """class for groups"""
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.String, unique=False)
    name = db.Column(db.String, unique=True)
    date_created = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
class GroupInfo(db.Model):
    """class for group playlists"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    group_id = db.Column(db.String(120), unique=False, nullable=False)
    playlist = db.Column(db.String(150), unique=False, nullable=True)
    url = db.Column(db.String(150), unique=False, nullable=True)
    comments = db.Column(db.String, unique=False, nullable=True)

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

for i in groups:
    the_new_group = Group(
        group_id=i['id'],
        name=i['name'],
        date_created=i['date_created'],
        description=i['description']
        )
    check_groups=Group.query.filter_by().all()
    if len(check_groups) >= 4:
        print("group database already populated")
    else:
        db.session.add(the_new_group)
        db.session.commit()

@bp.route("/")
def index():
    """initial react page"""
    return flask.render_template("index.html")

@bp.route("/home", methods=["POST", "GET"])
def homepage():
    """gets group page"""
    if flask.request.method == "POST":
        group_name = flask.request.form["Gname"]
        description = flask.request.form["group_description"]
        group = Group.query.filter_by().all()
        new_id = len(group) + 1
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        this_new_group = Group(group_id=new_id, name=group_name, date_created=dt_string, description=description)
        db.session.add(this_new_group)
        db.session.commit()
    all_groups = Group.query.filter_by().all()
    return flask.render_template("home.html", groups=all_groups)

@bp.route("/delPlaylist/<int:group_id>", methods=["POST", "GET"])
def del_playlist(group_id):
    "deletes playlists"
    user_playlists = Playlists.query.filter_by(username=user_id[0]).all()
    if flask.request.method == "POST":
        del_pl_name = flask.request.form["delete_playlist_name"]
        del_pl_url = flask.request.form["delete_playlist_url"]
        if del_pl_name and del_pl_url:
            check_pl = GroupInfo.query.filter_by(group_id=str(group_id), url=del_pl_url).all()
            if len(check_pl) < 1:
                print("this playlist does not exist")
            else:
                db.session.delete(check_pl[0])
                db.session.commit()
    group_info = GroupInfo.query.filter_by(group_id=str(group_id)).all()
    comments = []
    playlists = []
    for j in group_info:
        if j.comments:
            comments.append(j)
        if j.url:
            playlists.append(j)
    group = Group.query.filter_by(group_id=str(group_id)).all()
    return flask.render_template(
        "group.html",
        group=group[0],
        user_playlists=user_playlists,
        comments=comments,
        playlist=playlists,
        group_id=group_id,
    )

@bp.route("/post_comments/<int:group_id>", methods=["POST", "GET"])
def post_comment(group_id):
    """Post a comment"""
    user_playlists = Playlists.query.filter_by(username=user_id[0]).all()
<<<<<<< HEAD
    group_playlists = GroupInfo.query.filter_by(group_id=str(group_id)).all()
    group = next((group for group in groups if group["id"] == group_id), None)
    if group is None:
        flask.abort(404, description="No Group was Found with the given ID")
=======
    if flask.request.method == "POST":
        comment = flask.request.form["comment"]
        new_comment = GroupInfo(username=user_id[0], group_id=group_id, comments=comment)
        db.session.add(new_comment)
        db.session.commit()
    group_info = GroupInfo.query.filter_by(group_id=str(group_id)).all()
    comments = []
    playlists = []
    for j in group_info:
        if j.comments:
            comments.append(j)
        if j.url:
            playlists.append(j)
    group = Group.query.filter_by(group_id=str(group_id)).all()
>>>>>>> 813ffab58f44e5aabd2424c960bb95420f67a354
    return flask.render_template(
        "group.html",
        group=group[0],
        user_playlists=user_playlists,
        comments=comments,
        playlist=playlists,
        group_id=group_id,
    )

@bp.route("/group/<int:group_id>", methods=["GET", "POST"])
def group_details(group_id):
    """gets group details"""
    user_playlists = Playlists.query.filter_by(username=user_id[0]).all()
    if flask.request.method == "POST":
        print("Im here")
        add_pl_url = flask.request.form["add_playlist_url"]
        add_pl_name = flask.request.form["add_playlist_name"]
        if add_pl_url and add_pl_name:
            pl_exists = GroupInfo.query.filter_by(group_id=str(group_id), url=add_pl_url).all()
            if len(pl_exists) >= 1:
                print("this playlist already exists in this group")
            else:
                new_group_pl = GroupInfo(username=user_id[0], group_id=str(group_id), playlist=add_pl_name, url=add_pl_url)
                db.session.add(new_group_pl)
                db.session.commit()
<<<<<<< HEAD
    group_playlists = GroupInfo.query.filter_by(group_id=str(group_id)).all()
    # group = next((group for group in groups if group["id"] == group_id), None)
    # if group is None:
    #     flask.abort(404, description="No Group was Found with the given ID")
=======
    group_info = GroupInfo.query.filter_by(group_id=str(group_id)).all()
    comments = []
    playlists = []
    for j in group_info:
        if j.comments:
            comments.append(j)
        if j.url:
            playlists.append(j)
>>>>>>> 813ffab58f44e5aabd2424c960bb95420f67a354
    group = Group.query.filter_by(group_id=str(group_id)).all()
    return flask.render_template(
        "group.html",
        group=group[0],
        user_playlists=user_playlists,
        comments=comments,
        playlist=playlists,
        group_id=group_id,
    )

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
    user_id[0] = current_id
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
                username=playlist_id, playlist=playlist_name, url=playlist_url,
            )
            db.session.add(new_playlist)
            db.session.commit()
    return flask.jsonify(
        [
            {"PlaylistNames": playlist_names},
        ]
    )



app.register_blueprint(bp)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8000")))
# app.run()

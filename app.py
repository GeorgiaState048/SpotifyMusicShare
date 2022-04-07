"""app file"""
import os
import random
import flask
import json
import requests
from flask_sqlalchemy import SQLAlchemy

access = []
user_id = [' ']

app = flask.Flask(__name__)
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "this is a secret key!!!"

db = SQLAlchemy(app)


class AllData(db.Model):
    """class person"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    image = db.Column(db.String(150), unique=False, nullable=False)


# db.create_all()

# routes interpret different pages of a page
# @bp.route("/")
# def index():
#     """initial html page""
#     return flask.render_template("newIndex.html")


@bp.route("/")
def index():
    """initial react page"""
    return flask.render_template("index.html")

@bp.route('/get_access_token', methods=["GET", "POST"])
def get_access_token():
    """gets access token"""
    # i created a variable called access that holds the access token
    # this variable is populated as soon as the app loads
    if flask.request.method == "POST":
        info = json.loads(flask.request.data)
        access.append(info['token'])
    return access[0]

@bp.route("/user_info", methods=["GET", "POST"])
def get_user_info():
    """gets current user info"""
    user_endpoint = "https://api.spotify.com/v1/me"
    response = requests.get(
            user_endpoint,
            headers={
                "Authorization": "Bearer " + access[1],
            },
        )
    response_json = response.json()
    user = response_json["display_name"]
    images = response_json["images"][0]["url"]
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
                "Authorization": "Bearer " + access[1],
            },
        )
    response_json = response.json()
    items = response_json['items']
    playlist_names = []
    # adds all user playlist names to the returned json file. 
    for i in items:
        playlist_names.append(i['name'])
    return flask.jsonify([
        {"PlaylistNames": playlist_names},
    ])


app.register_blueprint(bp)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8000)))
# app.run()

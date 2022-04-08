
import os
import random
import flask
from flask_sqlalchemy import SQLAlchemy

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
#dummy API
groups = [
            {"id": 1, "name": "Jazz Lover", "date_created": "5 weeks", "description": "For Jazz Music."},
            {"id": 2, "name": "Music Recommendation", "date_created": "8 months", "description": "Group for music recommnedation. Drop your sickest beat here."},
            {"id": 3, "name": "Chill lofi", "date_created": "1 year", "description": "Collection of chill Lofi music. Check us out!"},
            {"id": 4, "name": "Justin Beiber's Anti-Fan Club", "date_created": "5 years", "description": "'nuff said."}, 
        ]
#MODEL, will put in a seperate file later
class group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    date_created = db.Column(db.String)
    description = db.Column(db.String)
    posted_by =  db.Column(db.String, db.ForeignKey('user.id'))
# routes interpret different pages of a page
# @bp.route("/")
# def index():
#     """initial html page""
#     return flask.render_template("newIndex.html")

@bp.route("/")
def index():
    """initial react page"""
    return flask.render_template("index.html")
@bp.route("/home",methods=["POST", "GET"])
def homepage():
    if flask.request.method == "POST":
        group_name = flask.request.form["Gname"]
        description = flask.request.form["group_description"]
        new_id = len(groups)+1
        new_group =  {"id": new_id, "name": group_name, "date_created": "just now", "description": description}
        groups.append(new_group)
    return flask.render_template("home.html",groups = groups)

@bp.route("/group/<int:group_id>")
def group_details(group_id):
    group = next((group for group in groups if group["id"] == group_id),None)
    if group is None: 
        abort(404, description="No Group was Found with the given ID")
    return flask.render_template("group.html", group = group)
app.register_blueprint(bp)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8000)))
# app.run()
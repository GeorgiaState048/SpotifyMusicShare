#flask test
from test.unit.webapp import client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    # Check that links to `about` and `login` pages exist
    assert "<a href=\"/about/\">About</a>" in html
    assert " <a href=\"/home/\">Login</a>" in html

    # Spot check important text
    assert "At CultureMesh, we're building networks to match these " \
           "real-world dynamics and knit the diverse fabrics of our world " \
           "together." in html
    assert "1. Join a network you belong to." in html

    assert landing.status_code == 200


def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/index/").data == landing.data

#test database
#test user
def test_new_group():
"""
GIVEN a group model
WHEN a group  is created
THEN check if everything is correct.
"""
group = Group('Test group', 'this is a test group','Danny')
    assert group.name == 'Test group'
    assert group.description == 'this is a test group'
    assert group.date_created = 'just now'
    assert group.posted_by == 'Danny'

def test_person():
    person = Person('Daniel')
    assert person.username = 'Daniel'


def test_playlist():
    playlist = Playlist('Daniel','Down to code')
    assert playlist.username = 'Daniel'
    assert playlist.playlist = 'Down to code'

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

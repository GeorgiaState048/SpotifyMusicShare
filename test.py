# pylint: disable=unused-import
# pylint: disable=undefined-variable
# pylint: disable=redefined-outer-name
# pylint: disable=unused-variable
# pylint: disable=no-name-in-module
# pylint: disable=import-error

#flask test
"""library for unitesting"""
from test.unit.webapp import client


def test_landing(client):
    """test landing"""
    landing = client.get("/")
    html = landing.data.decode()

    assert landing.status_code == 200


def test_landing_aliases(client):
    """landing data"""
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
    assert group.date_created == 'just now'
    assert group.posted_by == 'Danny'

def test_person():
    """testing person"""
    person = Person('Daniel')
    assert person.username == 'Daniel'


def test_playlist():
    """testing playlist"""
    playlist = Playlist('Daniel','Down to code')
    assert playlist.username == 'Daniel'
    assert playlist.playlist == 'Down to code'

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

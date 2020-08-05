from snowflake_data_profiler.app import app
import pytest


@pytest.fixture(scope='module')
def tester():

    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_get_profile(tester):

    # ensure flask set up correctly
    response = tester.get('/', content_type='html/text')
    assert response.status_code == 200

    # ensure flask set up correctly
    response = tester.get('/notreal', content_type='html/text')
    assert response.status_code == 404







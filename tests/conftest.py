from app import app
import pytest

@pytest.fixture(scope='function')
def client():
    """Setup an app client, this gets executed for each test function
    """
    yield app.test_client()
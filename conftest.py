import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    """Base URL for all API requests."""
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    """Shared requests session for all tests."""
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    yield s
    s.close()

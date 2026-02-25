import requests
import re

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_status_200():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_users_returns_list():
    response = requests.get(f"{BASE_URL}/users")
    assert isinstance(response.json(), list)

def test_get_users_not_empty():
    response = requests.get(f"{BASE_URL}/users")
    assert len(response.json()) > 0

def test_get_users_has_required_fields():
    user = requests.get(f"{BASE_URL}/users").json()[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "username" in user

def test_get_users_email_format_valid():
    users = requests.get(f"{BASE_URL}/users").json()
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    for user in users:
        assert email_pattern.match(user["email"]), f"Invalid email: {user['email']}"

def test_get_user_by_id_status_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_get_user_by_id_correct_id():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json()["id"] == 1

def test_get_user_nonexistent_404():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404

def test_get_user_has_address():
    user = requests.get(f"{BASE_URL}/users/1").json()
    assert "address" in user

def test_get_user_has_company():
    user = requests.get(f"{BASE_URL}/users/1").json()
    assert "company" in user

def test_get_users_returns_10_items():
    response = requests.get(f"{BASE_URL}/users")
    assert len(response.json()) == 10

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# --- GET /posts ---

def test_get_posts_status_200():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_posts_returns_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert isinstance(data, list)

def test_get_posts_not_empty():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert len(data) > 0

def test_get_posts_has_required_fields():
    response = requests.get(f"{BASE_URL}/posts")
    post = response.json()[0]
    assert "id" in post
    assert "title" in post
    assert "body" in post
    assert "userId" in post

def test_get_posts_content_type_json():
    response = requests.get(f"{BASE_URL}/posts")
    assert "application/json" in response.headers["Content-Type"]

def test_get_posts_returns_100_items():
    response = requests.get(f"{BASE_URL}/posts")
    assert len(response.json()) == 100


# --- GET /posts/{id} ---

def test_get_post_by_id_status_200():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_by_id_correct_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.json()["id"] == 1

def test_get_post_by_id_title_not_empty():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.json()["title"] != ""

def test_get_post_nonexistent_404():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404


# --- POST /posts ---

def test_create_post_status_201():
    payload = {"title": "Test", "body": "Body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

def test_create_post_returns_id():
    payload = {"title": "Test", "body": "Body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert "id" in response.json()

def test_create_post_fields_match():
    payload = {"title": "My Title", "body": "My Body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()
    assert data["title"] == "My Title"
    assert data["body"] == "My Body"


# --- PUT /posts/{id} ---

def test_update_post_status_200():
    payload = {"id": 1, "title": "Updated", "body": "Updated body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200

def test_update_post_title_updated():
    payload = {"id": 1, "title": "Updated Title", "body": "Body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.json()["title"] == "Updated Title"


# --- DELETE /posts/{id} ---

def test_delete_post_status_200():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_comments_status_200():
    response = requests.get(f"{BASE_URL}/comments")
    assert response.status_code == 200

def test_get_comments_returns_list():
    response = requests.get(f"{BASE_URL}/comments")
    assert isinstance(response.json(), list)

def test_get_comments_not_empty():
    response = requests.get(f"{BASE_URL}/comments")
    assert len(response.json()) > 0

def test_get_comments_has_required_fields():
    comment = requests.get(f"{BASE_URL}/comments").json()[0]
    assert "id" in comment
    assert "postId" in comment
    assert "name" in comment
    assert "email" in comment
    assert "body" in comment

def test_get_comment_by_id_status_200():
    response = requests.get(f"{BASE_URL}/comments/1")
    assert response.status_code == 200

def test_get_comment_by_id_correct_id():
    response = requests.get(f"{BASE_URL}/comments/1")
    assert response.json()["id"] == 1

def test_get_comment_nonexistent_404():
    response = requests.get(f"{BASE_URL}/comments/9999")
    assert response.status_code == 404

def test_filter_comments_by_postid():
    response = requests.get(f"{BASE_URL}/comments?postId=1")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0
    for comment in comments:
        assert comment["postId"] == 1

def test_filter_comments_returns_list():
    response = requests.get(f"{BASE_URL}/comments?postId=2")
    assert isinstance(response.json(), list)

def test_comments_email_not_empty():
    comments = requests.get(f"{BASE_URL}/comments").json()
    for comment in comments[:5]:
        assert comment["email"] != ""

def test_get_comments_returns_500_items():
    response = requests.get(f"{BASE_URL}/comments")
    assert len(response.json()) == 500

# 🧪 QA API Tests — JSONPlaceholder

Practice API test suite built with **Python + pytest + requests**.  
Tests cover a public REST API: [JSONPlaceholder](https://jsonplaceholder.typicode.com)

---

## 📁 Project Structure

```
qa-api-tests/
│
├── tests/
│   ├── test_posts.py       # Tests for /posts endpoint
│   ├── test_users.py       # Tests for /users endpoint
│   └── test_comments.py    # Tests for /comments endpoint
│
├── conftest.py             # Fixtures (base URL, session)
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/Ilya011/qa-api-tests.git
cd qa-api-tests

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests
pytest -v

# 4. Run specific file
pytest tests/test_posts.py -v

# 5. Run with report
pytest -v --tb=short
```

---

## ✅ What's Tested

| Endpoint | Method | Test Cases |
|----------|--------|------------|
| `/posts` | GET | Status 200, response is list, fields present |
| `/posts/1` | GET | Status 200, correct ID returned |
| `/posts/9999` | GET | Status 404 for non-existent resource |
| `/posts` | POST | Status 201, created object returned |
| `/posts/1` | PUT | Status 200, updated fields returned |
| `/posts/1` | DELETE | Status 200 |
| `/users` | GET | Status 200, email format valid |
| `/comments` | GET | Status 200, postId filter works |

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **pytest** — test framework
- **requests** — HTTP client

---

*Part of my QA portfolio. Learning Python test automation.*  
*Author: Ilya Shlegel · [LinkedIn](https://www.linkedin.com/in/ilya-shlegel-5325143ab/) · [Telegram](https://t.me/director011)*

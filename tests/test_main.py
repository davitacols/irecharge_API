import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_article():
    data = {
        "article_no": 105,
        "currency": "US Dollar",
        "provider_no": "0010",
        "provider": "PayStack",
        "price": 1500
    }

    response = requests.post(f"{BASE_URL}/articles/", json=data)
    assert response.status_code == 200

    # Access the returned data and assert
    returned_data = response.json()
    assert returned_data["article_no"] == data["article_no"]


def test_read_articles():
    response = requests.get(f"{BASE_URL}/articles/")
    assert response.status_code == 200

    # Access the returned data and perform assertions
    articles = response.json()
    assert isinstance(articles, list)


def test_read_article():
    article_no = 105  # existing article number
    response = requests.get(f"{BASE_URL}/articles/{article_no}")
    assert response.status_code == 200

    # Access the returned data and assert
    returned_data = response.json()
    assert returned_data["article_no"] == article_no


def test_update_article():
    data = {
        "price": 79.99
    }

    response = requests.put(f"{BASE_URL}/articles/105", json=data)
    assert response.status_code == 200

    # Access the returned data and assert
    returned_data = response.json()
    assert returned_data["price"] == 79.99


def test_delete_article():
    response = requests.delete(f"{BASE_URL}/articles/105")
    assert response.status_code == 200

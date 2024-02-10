from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from .main import app, get_db

client = TestClient(app)

# Test data
test_article_data = {
    "article_no": 1,
    "currency": "USD",
    "provider_no": "123",
    "provider": "Test Provider",
    "price": 10.99,
}


def test_create_article():
    response = client.post("/articles/", json=test_article_data)
    assert response.status_code == 200
    assert response.json() == test_article_data


def test_read_articles():
    response = client.get("/articles/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_article():
    response = client.get("/articles/1")
    assert response.status_code == 200
    assert response.json() == test_article_data


def test_update_article():
    updated_data = {
        "article_no": 1,
        "currency": "EUR",
        "provider_no": "456",
        "provider": "Updated Provider",
        "price": 15.99,
    }
    response = client.put("/articles/1", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data


def test_delete_article():
    response = client.delete("/articles/1")
    assert response.status_code == 200
    assert response.json() == test_article_data


# Additional cleanup if needed
def delete_test_data(db: Session):
    test_article = db.query(ArticleDB).filter(ArticleDB.article_no == 1).first()
    if test_article:
        db.delete(test_article)
        db.commit()


# Run cleanup before running tests
delete_test_data(get_db())


# Run tests
test_create_article()
test_read_articles()
test_read_article()
test_update_article()
test_delete_article()

# Run cleanup after running tests
delete_test_data(get_db())

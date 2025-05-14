import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_create_user_valid(client):
    res = client.post("/users", json={
        "firstName": "Anna",
        "lastName": "Nowak",
        "birthYear": 1990,
        "group": "admin"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["firstName"] == "Anna"
    assert "age" in data

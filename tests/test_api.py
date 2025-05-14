import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_user_api(client):
    res = client.post("/users", json={
        "firstName": "Ewa",
        "lastName": "Zielińska",
        "birthYear": 1985,
        "group": "user"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["firstName"] == "Ewa"
    assert "age" in data

def test_create_user_invalid_data(client):
    res = client.post("/users", json={
        "firstName": "Tom",
        "lastName": "X",
        "birthYear": 2000,
        "group": "invalid_role"
    })
    assert res.status_code == 400
    assert "Invalid group" in res.get_json()["error"]

def test_get_user_not_found(client):
    res = client.get("/users/999")
    assert res.status_code == 404

def test_user_lifecycle(client):
    # Create
    res = client.post("/users", json={
        "firstName": "Ala",
        "lastName": "Kowal",
        "birthYear": 1995,
        "group": "premium"
    })
    assert res.status_code == 201
    user = res.get_json()
    user_id = user["id"]

    # Get
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200

    # Update
    res = client.patch(f"/users/{user_id}", json={"group": "admin"})
    assert res.status_code == 200
    assert res.get_json()["group"] == "admin"

    # Delete
    res = client.delete(f"/users/{user_id}")
    assert res.status_code == 204

    # Confirm deletion
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 404

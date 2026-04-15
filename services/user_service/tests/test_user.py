from fastapi.testclient import TestClient

from services.user_service.app.main import app


client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_register_and_login():
    user_data = {
        "email": "test@test.com",
        "password": "123456"
    }

    # register
    response = client.post("/register", json=user_data)
    assert response.status_code in [200, 400]  # might be already registered

    # login
    response = client.post("/login", json=user_data)
    assert response.status_code == 200

    token = response.json()["access_token"]
    assert token is not None


def test_me_endpoint():
    user_data = {
        "email": "test2@test.com",
        "password": "123456"
    }

    # register
    client.post("/register", json=user_data)

    # login
    response = client.post("/login", json=user_data)
    token = response.json()["access_token"]

    # me
    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

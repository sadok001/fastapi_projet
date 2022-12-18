from fastapi.testclient import TestClient

from domain.user.user import User
from infrastructure.utils.hasher import Hasher
from main import app

client = TestClient(app)


user = User(
    first_name="test",
    last_name="test",
    email="test@gmail.com"
)


def test_password_hashed_correctly() -> None:
    user.set_password("test")

    assert Hasher.verify_password("test", user.get_password())


def test_user_has_valid_code() -> None:
    user.set_code()
    code = user.get_code()

    assert code >= 1000 and code <= 9999


def test_create_user():
    data = {
        "first_name": "test001",
        "last_name": "test001",
        "email": "test001@example.com",
        "password": "test001",
        "confirm_password": "test001"
    }

    response = client.post("/api/v1/users/", json=data)
    
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "test001",
        "last_name": "test001",
        "email": "test001@example.com"
    }

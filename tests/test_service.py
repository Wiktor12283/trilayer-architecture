import pytest
from service.user_service import UserService
from repository.user_repository import UserRepository

@pytest.fixture
def service():
    return UserService(UserRepository())

def test_create_user_valid(service):
    data = {
        "firstName": "Jan",
        "lastName": "Kowalski",
        "birthYear": 1990,
        "group": "admin"
    }
    user = service.create_user(data)
    assert user.id == 1
    assert user.first_name == "Jan"

def test_create_user_invalid_group(service):
    data = {
        "firstName": "Anna",
        "lastName": "Nowak",
        "birthYear": 1992,
        "group": "vip"
    }
    with pytest.raises(ValueError, match="Invalid group"):
        service.create_user(data)

def test_get_user_not_found(service):
    user = service.get_user(999)
    assert user is None

def test_update_user_group(service):
    user = service.create_user({
        "firstName": "Jan",
        "lastName": "Kowalski",
        "birthYear": 1990,
        "group": "user"
    })
    updated = service.update_user(user.id, {"group": "premium"})
    assert updated.group == "premium"

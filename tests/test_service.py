from service.user_service import UserService
from repository.user_repository import UserRepository


def test_create_user_valid():
    repo = UserRepository()
    service = UserService(repo)
    user = service.create_user({
        "firstName": "Anna",
        "lastName": "Nowak",
        "birthYear": 1990,
        "group": "user"
    })
    assert user.id == 1

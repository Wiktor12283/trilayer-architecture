from datetime import datetime
from models.user import User, VALID_GROUPS

class UserService:
    def __init__(self, repository):
        self.repo = repository

    def create_user(self, data):
        self._validate_user_data(data)
        user = User(
            id=0,
            first_name=data["firstName"],
            last_name=data["lastName"],
            birth_year=data["birthYear"],
            group=data["group"]
        )
        return self.repo.add(user)

    def get_all_users(self):
        return self.repo.get_all()

    def get_user(self, user_id):
        return self.repo.get_by_id(user_id)

    def update_user(self, user_id, data):
        if "group" in data and data["group"] not in VALID_GROUPS:
            raise ValueError("Invalid group value")
        return self.repo.update(user_id, data)

    def delete_user(self, user_id):
        return self.repo.delete(user_id)

    def _validate_user_data(self, data):
        required_fields = {"firstName", "lastName", "birthYear", "group"}
        if not required_fields.issubset(data):
            raise ValueError("Missing required fields")
        if not isinstance(data["birthYear"], int):
            raise ValueError("Invalid birthYear")
        if data["group"] not in VALID_GROUPS:
            raise ValueError("Invalid group")

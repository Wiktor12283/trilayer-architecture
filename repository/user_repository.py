class UserRepository:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def add(self, user):
        user.id = self.next_id
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def get_all(self):
        return list(self.users.values())

    def get_by_id(self, user_id):
        return self.users.get(user_id)

    def update(self, user_id, data):
        user = self.users.get(user_id)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        return user

    def delete(self, user_id):
        return self.users.pop(user_id, None)

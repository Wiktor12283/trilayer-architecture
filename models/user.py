from dataclasses import dataclass

VALID_GROUPS = {"user", "premium", "admin"}

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    birth_year: int
    group: str

    def to_dict(self, current_year: int):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "age": current_year - self.birth_year,
            "group": self.group
        }

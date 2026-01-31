class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    def get_max_books(self):
        return 0  # polymorphism

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.__class__.__name__
        }

    @staticmethod
    def from_dict(data):
        if data["type"] == "Student":
            return Student(data["id"], data["name"])
        elif data["type"] == "Teacher":
            return Teacher(data["id"], data["name"])

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] {self.name}"


class Student(User):
    def get_max_books(self):
        return 3


class Teacher(User):
    def get_max_books(self):
        return 10

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def get_max_loans(self):
        return 3  # default

    def __str__(self):
        return f"[{self.user_id}] {self.name}"


class Student(User):
    def get_max_loans(self):
        return 3


class Teacher(User):
    def get_max_loans(self):
        return 5

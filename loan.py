from book import Book
from user import User


class Loan:
    def __init__(self, book: Book, user: User):
        self.book = book
        self.user = user

    def __str__(self):
        return f"{self.book.title} loaned to {self.user.name}"

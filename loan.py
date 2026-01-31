class Loan:
    def __init__(self, book, user):
        self.book = book
        self.user = user

    def __str__(self):
        return f"Loan: {self.book.title} -> {self.user.name}"

    def to_dict(self):
        return {
            "book_id": self.book.id,
            "user_id": self.user.id
        }

    @staticmethod
    def from_dict(data, books, users):
        book = next(b for b in books if b.id == data["book_id"])
        user = next(u for u in users if u.id == data["user_id"])
        return Loan(book, user)

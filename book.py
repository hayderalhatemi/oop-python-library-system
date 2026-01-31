class Book:
    def __init__(self, book_id, title, author, available=True):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Book[{self.id}] {self.title} by {self.author} - {status}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["id"],
            data["title"],
            data["author"],
            data["available"]
        )

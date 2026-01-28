class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "On loan"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

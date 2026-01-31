import json
from book import Book
from user import Student, Teacher
from loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []
        self.load_from_file()

    # ---------- Core logic ----------

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()

    def add_user(self, user):
        self.users.append(user)
        self.save_to_file()

    def borrow_book(self, book_id, user_id):
        book = next((b for b in self.books if b.id == book_id and b.available), None)
        user = next((u for u in self.users if u.id == user_id), None)

        if not book or not user:
            return "Book or user not found."

        # Polymorphism in action
        user_loans = [l for l in self.loans if l.user.id == user.id]
        if len(user_loans) >= user.get_max_books():
            return f"{user.name} has reached the borrowing limit."

        book.available = False
        loan = Loan(book, user)
        self.loans.append(loan)
        self.save_to_file()
        return "Book borrowed successfully."

    def return_book(self, book_id):
        loan = next((l for l in self.loans if l.book.id == book_id), None)
        if not loan:
            return "Loan not found."

        loan.book.available = True
        self.loans.remove(loan)
        self.save_to_file()
        return "Book returned successfully."

    def list_books(self):
        return self.books

    def list_loans(self):
        return self.loans

    # ---------- File handling (JSON) ----------

    def save_to_file(self):
        data = {
            "books": [b.to_dict() for b in self.books],
            "users": [u.to_dict() for u in self.users],
            "loans": [l.to_dict() for l in self.loans]
        }

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

            self.books = [Book.from_dict(b) for b in data.get("books", [])]

            self.users = []
            for u in data.get("users", []):
                if u["type"] == "Student":
                    self.users.append(Student.from_dict(u))
                else:
                    self.users.append(Teacher.from_dict(u))

            self.loans = []
            for l in data.get("loans", []):
                book = next(b for b in self.books if b.id == l["book_id"])
                user = next(u for u in self.users if u.id == l["user_id"])
                self.loans.append(Loan(book, user))

        except FileNotFoundError:
            pass

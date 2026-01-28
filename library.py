from book import Book
from user import User
from loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def find_book(self, book_id: int):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_user(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def borrow_book(self, book_id: int, user_id: int):
        book = self.find_book(book_id)
        user = self.find_user(user_id)

        if not book or not user:
            return "Book or user not found."

        user_loans = [loan for loan in self.loans if loan.user == user]
        if len(user_loans) >= user.get_max_loans():
            return "User has reached maximum loan limit."

        if book.borrow():
            loan = Loan(book, user)
            self.loans.append(loan)
            return "Book borrowed successfully."
        else:
            return "Book is not available."

    def return_book(self, book_id: int):
        for loan in self.loans:
            if loan.book.book_id == book_id:
                loan.book.return_book()
                self.loans.remove(loan)
                return "Book returned."
        return "Loan not found."

    def list_books(self):
        return [str(book) for book in self.books]

    def list_loans(self):
        return [str(loan) for loan in self.loans]

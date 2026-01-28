from book import Book
from user import Student, Teacher
from library import Library


def main():
    library = Library()

    # Add books
    library.add_book(Book(1, "1984", "George Orwell"))
    library.add_book(Book(2, "Clean Code", "Robert Martin"))

    # Add users
    library.add_user(Student(1, "Alice"))
    library.add_user(Teacher(2, "Bob"))

    print("Books:")
    for b in library.list_books():
        print(b)

    print("\nBorrowing book 1 by Alice:")
    print(library.borrow_book(1, 1))

    print("\nBorrowing book 2 by Bob:")
    print(library.borrow_book(2, 2))

    print("\nLoans:")
    for l in library.list_loans():
        print(l)

    print("\nReturning book 1:")
    print(library.return_book(1))

    print("\nBooks:")
    for b in library.list_books():
        print(b)


if __name__ == "__main__":
    main()

from book import Book
from user import Student, Teacher
from library import Library


def print_menu():
    print("\n--- Library Menu ---")
    print("1. Add book")
    print("2. Add user")
    print("3. Borrow book")
    print("4. Return book")
    print("5. List books")
    print("6. List loans")
    print("0. Exit")


def main():
    library = Library()  # loads data.json automatically

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            book_id = int(input("Book ID: "))
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(Book(book_id, title, author))
            print("Book added.")

        elif choice == "2":
            user_id = int(input("User ID: "))
            name = input("Name: ")
            user_type = input("Type (student/teacher): ").lower()

            if user_type == "student":
                library.add_user(Student(user_id, name))
            elif user_type == "teacher":
                library.add_user(Teacher(user_id, name))
            else:
                print("Invalid user type.")
                continue

            print("User added.")

        elif choice == "3":
            book_id = int(input("Book ID: "))
            user_id = int(input("User ID: "))
            print(library.borrow_book(book_id, user_id))

        elif choice == "4":
            book_id = int(input("Book ID: "))
            print(library.return_book(book_id))

        elif choice == "5":
            print("\nBooks:")
            for book in library.list_books():
                print(book)

        elif choice == "6":
            print("\nLoans:")
            for loan in library.list_loans():
                print(loan)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

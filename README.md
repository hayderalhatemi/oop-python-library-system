# Library Management System (OOP Python)

This is a simple console-based Library Management System built with Python using Object-Oriented Programming.

## Project Description

The goal of this project is to demonstrate the use of Object-Oriented Programming concepts such as:
- Multiple classes and modules
- Inheritance and polymorphism
- Associations between objects
- Data structures
- File persistence using JSON

The system allows adding books and users, borrowing and returning books, and automatically saving data between program runs.


## Features
- Add books  
- Add users (students and teachers)  
- Borrow and return books  
- View available books  
- View active loans  

## Technologies
- Python 3  
- Object-Oriented Programming  

## How to run
```bash
python main.py

## Author

Hayder Alhatemi

## UML Diagrams

                +----------------+
                |     Book       |
                +----------------+
                | id             |
                | title          |
                | author         |
                | available      |
                +----------------+
                | to_dict()      |
                | from_dict()    |
                | __str__()      |
                +----------------+

                +----------------+
                |     User       |
                +----------------+
                | id             |
                | name           |
                +----------------+
                | get_max_books()|
                | to_dict()      |
                | from_dict()    |
                | __str__()      |
                +----------------+
                     ▲
        -----------------------------
        |                           |
+----------------+        +----------------+
|    Student     |        |    Teacher     |
+----------------+        +----------------+
| get_max_books()|        | get_max_books()|
+----------------+        +----------------+

                +----------------+
                |     Loan       |
                +----------------+
                | book           |
                | user           |
                +----------------+
                | to_dict()      |
                | from_dict()    |
                | __str__()      |
                +----------------+

                +----------------+
                |    Library     |
                +----------------+
                | books          |
                | users          |
                | loans          |
                +----------------+
                | add_book()     |
                | add_user()     |
                | borrow_book()  |
                | return_book()  |
                | list_books()   |
                | list_loans()   |
                | save_to_file() |
                | load_from_file()|
                +----------------+

Relationships:
Library 1 ---- * Book  
Library 1 ---- * User  
Library 1 ---- * Loan  

User <|-- Student  
User <|-- Teacher  

Loan ----> Book  
Loan ----> User  

### Sequence Diagram (Borrow Book)

User -> main.py : choose "Borrow book"  
main.py -> Library : borrow_book(book_id, user_id)  
Library -> Library : find book  
Library -> Library : find user  
Library -> User : get_max_books()  
Library -> Library : check current loans  

alt [limit not reached]  
    Library -> Book : available = False  
    Library -> Loan : create Loan(book, user)  
    Library -> Library : add loan to list  
    Library -> Library : save_to_file()  
    Library -> main.py : "Book borrowed successfully."  
else [limit reached]  
    Library -> main.py : "Borrowing limit reached"  
end  


### Flowchart (Main Menu Logic)

Start  
  ↓  
Display menu  
  ↓  
User chooses option  
  ↓  
Is choice = 1? ── Yes → Add book → Save → Back to menu  
        │  
        No  
        ↓  
Is choice = 2? ── Yes → Add user → Save → Back to menu  
        │  
        No  
        ↓  
Is choice = 3? ── Yes → Borrow book → Save → Back to menu  
        │  
        No  
        ↓  
Is choice = 4? ── Yes → Return book → Save → Back to menu  
        │  
        No  
        ↓  
Is choice = 5? ── Yes → List books → Back to menu  
        │  
        No  
        ↓  
Is choice = 6? ── Yes → List loans → Back to menu  
        │  
        No  
        ↓  
Is choice = 0? ── Yes → End  
        │  
        No  
        ↓  
Show "Invalid choice" → Back to menu

## Testing

## Testing

The system was tested manually using the console menu.  
The following test cases were executed:

### Test Case 1: Add Book
Input:
- Choose option 1
- Book ID = 1
- Title = "Python Basics"
- Author = "Guido"

Expected result:
- Book is added to the system
- Book appears in book list

Actual result:
- Book added successfully

Status: PASS


### Test Case 2: Add User (Student)
Input:
- Choose option 2
- User ID = 1
- Name = "Alice"
- Type = student

Expected result:
- User is added to the system

Actual result:
- User added successfully

Status: PASS


### Test Case 3: Borrow Book
Input:
- Choose option 3
- Book ID = 1
- User ID = 1

Expected result:
- Book becomes unavailable
- Loan is created

Actual result:
- Book borrowed successfully

Status: PASS


### Test Case 4: Borrow Limit (Polymorphism)
Input:
- Student borrows more than allowed books

Expected result:
- System prevents borrowing
- Error message shown

Actual result:
- Borrowing limit reached

Status: PASS


### Test Case 5: Return Book
Input:
- Choose option 4
- Book ID = 1

Expected result:
- Book becomes available
- Loan is removed

Actual result:
- Book returned successfully

Status: PASS


### Test Case 6: JSON Save & Load
Steps:
- Add book and user
- Exit program
- Restart program

Expected result:
- Data is loaded from data.json
- Books, users and loans persist

Actual result:
- Data loaded correctly

Status: PASS

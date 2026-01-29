# Library Management System (OOP Python)

This is a simple console-based Library Management System built with Python using Object-Oriented Programming.

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

## UML Diagram

Library

books

users

loans

add_book()

add_user()

borrow_book()

return_book()

Book

id

title

author

available

User

id

name

Student : User
Teacher : User

Loan

book

user
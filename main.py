import re

# Class to represent a book in the library
class Book:
    def __init__(self, title, author, genre, publication_date):
        # Initialize book attributes
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True  # Book is available by default

    # Method to borrow a book
    def borrow(self):
        if self.__availability:
            self.__availability = False  # Mark book as unavailable
            return True
        return False  # Return False if book is already borrowed

    # Method to return a book
    def return_book(self):
        self.__availability = True  # Mark book as available

    # Check if the book is available
    def is_available(self):
        return self.__availability

    # Get details of the book
    def get_details(self):
        return {
            'title': self.__title,
            'author': self.__author,
            'genre': self.__genre,
            'publication_date': self.__publication_date,
            'availability': self.__availability
        }


# Class to represent a user in the library
class User:
    def __init__(self, name, library_id):
        # Initialize user attributes
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []  # List to track borrowed books

    # Method for user to borrow a book
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    # Method for user to return a borrowed book
    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)

    # Get details of the user
    def get_details(self):
        return {
            'name': self.__name,
            'library_id': self.__library_id,
            'borrowed_books': self.__borrowed_books
        }


# Class to represent an author
class Author:
    def __init__(self, name, biography):
        # Initialize author attributes
        self.__name = name
        self.__biography = biography

    # Get details of the author
    def get_details(self):
        return {
            'name': self.__name,
            'biography': self.__biography
        }


# Class to represent the library system
class Library:
    def __init__(self):
        # Initialize lists for books, users, and authors
        self.books = []
        self.users = []
        self.authors = []

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Method to add a user to the library
    def add_user(self, user):
        self.users.append(user)

    # Method to add an author to the library
    def add_author(self, author):
        self.authors.append(author)

    # Method to search for a book by title
    def search_book(self, title):
        for book in self.books:
            if book.get_details()['title'].lower() == title.lower():
                return book  # Return the found book
        return None  # Return None if no book is found

    # Method to display all books in the library
    def display_books(self):
        return [book.get_details() for book in self.books]

    # Method to display all users in the library
    def display_users(self):
        return [user.get_details() for user in self.users]

    # Method to display all authors in the library
    def display_authors(self):
        return [author.get_details() for author in self.authors]


# Function to display the main menu and handle user input
def main_menu():
    print("Welcome to the Library Management System!")
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        
        choice = input("Select an option (1-4): ")
        if choice == '1':
            book_operations()  # Handle book operations
        elif choice == '2':
            user_operations()  # Handle user operations
        elif choice == '3':
            author_operations()  # Handle author operations
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")

# Function to handle book operations
def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Go back to main menu")

        choice = input("Select an option (1-6): ")
        if choice == '1':
            add_book()  # Function to add a new book
        elif choice == '2':
            borrow_book()  # Function to borrow a book
        elif choice == '3':
            return_book()  # Function to return a book
        elif choice == '4':
            search_book()  # Function to search for a book
        elif choice == '5':
            display_books()  # Function to display all books
        elif choice == '6':
            break  # Go back to main menu
        else:
            print("Invalid option. Please try again.")

# Function to handle user operations
def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Go back to main menu")

        choice = input("Select an option (1-4): ")
        if choice == '1':
            add_user()  # Function to add a new user
        elif choice == '2':
            view_user_details()  # Function to view user details
        elif choice == '3':
            display_users()  # Function to display all users
        elif choice == '4':
            break  # Go back to main menu
        else:
            print("Invalid option. Please try again.")

# Function to handle author operations
def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Go back to main menu")

        choice = input("Select an option (1-4): ")
        if choice == '1':
            add_author()  # Function to add a new author
        elif choice == '2':
            view_author_details()  # Function to view author details
        elif choice == '3':
            display_authors()  # Function to display all authors
        elif choice == '4':
            break  # Go back to main menu
        else:
            print("Invalid option. Please try again.")

# Initialize the library
library = Library()

# Function to add a new book to the library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    book = Book(title, author, genre, publication_date)  # Create a new book instance
    library.add_book(book)  # Add the book to the library
    print(f"Book '{title}' added successfully.")

# Function to borrow a book
def borrow_book():
    title = input("Enter book title to borrow: ")
    book = library.search_book(title)  # Search for the book
    if book and book.is_available():  # Check if the book is available
        user_id = input("Enter your library ID: ")
        user = next((u for u in library.users if u.get_details()['library_id'] == user_id), None)  # Find user by ID
        if user:
            book.borrow()  # Mark book as borrowed
            user.borrow_book(title)  # Add book to user's borrowed list
            print(f"You have borrowed '{title}'.")
        else:
            print("User not found.")  # Handle case where user is not found
    else:
        print("Book not available or not found.")

# Function to return a borrowed book
def return_book():
    title = input("Enter book title to return: ")
    book = library.search_book(title)  # Search for the book
    if book and not book.is_available():  # Check if the book is currently borrowed
        user_id = input("Enter your library ID: ")
        user = next((u for u in library.users if u.get_details()['library_id'] == user_id), None)  # Find user by ID
        if user and title in user.get_details()['borrowed_books']:  # Check if the user borrowed this book
            book.return_book()  # Mark book as returned
            user.return_book(title)  # Remove book from user's borrowed list
            print(f"You have returned '{title}'.")
        else:
            print("User not found or you did not borrow this book.")
    else:
        print("Book not found or already available.")

# Function to search for a book by title
def search_book():
    title = input("Enter book title to search: ")
    book = library.search_book(title)  # Search for the book
    if book:
        details = book.get_details()  # Get book details
        print(f"Book found: {details}")  # Display book details
    else:
        print("Book not found.")  # Handle case where book is not found

# Function to display all books in the library
def display_books():
    books = library.display_books()  # Get list of all books
    if books:
        for book in books:
            print(book)  # Print details of each book
    else:
        print("No books available.")  # Handle case where no books are available

# Function to add a new user to the library
def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    user = User(name, library_id)  # Create a new user instance
    library.add_user(user)  # Add the user to the library
    print(f"User '{name}' added successfully.")

# Function to view details of a specific user
def view_user_details():
    user_id = input("Enter library ID to view details: ")
    user = next((u for u in library.users if u.get_details()['library_id'] == user_id), None)  # Find user by ID
    if user:
        print(user.get_details())  # Print user details
    else:
        print("User not found.")  # Handle case where user is not found

# Function to display all users in the library
def display_users():
    users = library.display_users()  # Get list of all users
    if users:
        for user in users:
            print(user)  # Print details of each user
    else:
        print("No users available.")  # Handle case where no users are available

# Function to add a new author to the library
def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    author = Author(name, biography)  # Create a new author instance
    library.add_author(author)  # Add the author to the library
    print(f"Author '{name}' added successfully.")

# Function to view details of a specific author
def view_author_details():
    name = input("Enter author name to view details: ")
    author = next((a for a in library.authors if a.get_details()['name'].lower() == name.lower()), None)  # Find author by name
    if author:
        print(author.get_details())  # Print author details
    else:
        print("Author not found.")  # Handle case where author is not found

# Function to display all authors in the library
def display_authors():
    authors = library.display_authors()  # Get list of all authors
    if authors:
        for author in authors:
            print(author)  # Print details of each author
    else:
        print("No authors available.")  # Handle case where no authors are available

# Entry point of the program
if __name__ == "__main__":
    main_menu()  # Start the main menu

from datetime import datetime, timedelta
from time import sleep

class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, author, quantity):
        if title in self.books:
            self.books[title] = (author, self.books[title][1] + quantity)
        else:
            self.books[title] = (author, quantity)
        print(f'Book "{title}" added successfully!')

    def remove_book(self, title):
        try:
            if title in self.books:
                del self.books[title]
                print(f'Book "{title}" removed successfully!')
            else:
                raise KeyError("Book not found in the library.")
        except KeyError as e:
            print(e)

    def update_book(self, title, author=None, quantity=None):
        try:
            if title in self.books:
                current_author, current_quantity = self.books[title]
                self.books[title] = (author if author else current_author,
                                     quantity if quantity is not None else current_quantity)
                print(f'Book "{title}" updated successfully!')
            else:
                raise KeyError("Book not found in the library.")
        except KeyError as e:
            print(e)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for title, (author, quantity) in self.books.items():
                print(f'Title: {title}, Author: {author}, Quantity: {quantity}')

    def search_book(self, title):
        try:
            if title in self.books:
                author, quantity = self.books[title]
                print(f'Book Found - Title: {title}, Author: {author}, Quantity: {quantity}')
            else:
                raise KeyError("Book not found in the library.")
        except KeyError as e:
            print(e)

    def borrow_book(self, user_name, title):
        try:
            if title in self.books and self.books[title][1] > 0:
                if user_name not in self.borrowed_books:
                    self.borrowed_books[user_name] = {}

                if len(self.borrowed_books[user_name]) >= 2:
                    print("You can only borrow a maximum of 2 books at a time.")
                    return

                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=14)
                self.borrowed_books[user_name][title] = (borrow_date.strftime('%Y-%m-%d'), due_date.strftime('%Y-%m-%d'))
                self.books[title] = (self.books[title][0], self.books[title][1] - 1)
                print(f'Book "{title}" borrowed successfully by {user_name}! Due date: {due_date.strftime("%Y-%m-%d")}')
            else:
                raise KeyError("Book not available for borrowing.")
        except KeyError as e:
            print(e)

    def return_book(self, user_name, title):
        try:
            if user_name in self.borrowed_books and title in self.borrowed_books[user_name]:
                del self.borrowed_books[user_name][title]
                if not self.borrowed_books[user_name]:
                    del self.borrowed_books[user_name]

                self.books[title] = (self.books[title][0], self.books[title][1] + 1)
                print(f'Book "{title}" returned successfully by {user_name}!')
            else:
                raise KeyError("Book not borrowed or incorrect user.")
        except KeyError as e:
            print(e)

    def view_borrowed_books(self, user_name):
        if user_name in self.borrowed_books:
            print(f'Books borrowed by {user_name}:')
            for title, (borrow_date, due_date) in self.borrowed_books[user_name].items():
                print(f'Title: {title}, Borrowed on: {borrow_date}, Due on: {due_date}')
        else:
            print(f'No books borrowed by {user_name}.')

library = Library()
counter = 1
while True:
    sleep(3)
    print(
        "Library Management System"
        "\n1. Add Book"
        "\n2. Remove Book"
        "\n3. Update Book"
        "\n4. Display Books"
        "\n5. Search Book"
        "\n6. Borrow Book"
        "\n7. Return Book"
        "\n8. View Borrowed Books"
        "\n9. Exit"
    )

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        library.add_book(title, author, quantity)
    elif choice == "2":
        title = input("Enter book title to remove: ")
        library.remove_book(title)
    elif choice == "3":
        title = input("Enter book title to update: ")
        author = input("Enter new author (or press enter to keep the same): ") or None
        quantity = input("Enter new quantity (or press enter to keep the same): ")
        quantity = int(quantity) if quantity else None
        library.update_book(title, author, quantity)
    elif choice == "4":
        library.display_books()
    elif choice == "5":
        title = input("Enter book title to search: ")
        library.search_book(title)
    elif choice == "6":
        user_name = input("Enter your name: ")
        title = input("Enter book title to borrow: ")
        library.borrow_book(user_name, title)
    elif choice == "7":
        user_name = input("Enter your name: ")
        title = input("Enter book title to return: ")
        library.return_book(user_name, title)
    elif choice == "8":
        user_name = input("Enter your name: ")
        library.view_borrowed_books(user_name)
    elif choice == "9":
        print("Exiting the program...")
        break
    else:
        if counter < 3 :
            print(f"Invalid choice! You have selected wrong input for {counter} times! \nPlease enter a number between 1 and 9.")
            counter += 1
        else:
            print("You have exceded max no of retries! Program is Exiting! Thank You!")
            break

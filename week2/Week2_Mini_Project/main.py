from book import Book
from user import Student, Librarian
from library import Library
# creating library and a default user
lib = Library()
user = Student("Garima", "S001")
print(f"\nWelcome to Garima's Library System")
print(f"Logged in as: {user}\n")

while True:
    print("\nMAIN MENU")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")
    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        try:
            bid = input("Enter book ID: ").strip()
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            if not bid or not title or not author:
                print("all fields are required!")
            else:
                b = Book(bid, title, author)
                lib.add_book(b)
        except Exception as e:
            print(f"something went wrong: {e}")

    elif choice == "2":
        lib.view_books()

    elif choice == "3":
        bid = input("Enter book ID to borrow: ").strip()
        lib.borrow_book(bid, user)

    elif choice == "4":
        bid = input("Enter book ID to return: ").strip()
        lib.return_book(bid, user)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("invalid choice! please enter a number between 1-5")
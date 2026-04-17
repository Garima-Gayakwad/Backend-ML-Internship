import logging
# setting up logging - (all actions will get saved to library.log automatically)
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# custom exceptions - (more specific error types)
class BookNotFound(Exception):
    pass
class AlreadyBorrowed(Exception):
    pass
class NotBorrowed(Exception):
    pass

# Library class - manages all books and borrow/return logic
class Library:
    def __init__(self):
        self.__books = {}  # ENCAPSULATION - private dict, key = book_id

    def add_book(self, book): # adding a new book to library
        self.__books[book.book_id] = book
        logging.info(f"Book added: {book.title} by {book.author}")
        print(f"Book '{book.title}' added successfully!")

    def view_books(self): # showing all books
        if not self.__books:
            print("no books in the library yet!")
            return
        print("\nAll Books-")
        for b in self.__books.values():
            print(b)

    def borrow_book(self, book_id, user): # borrowing a book
        try:
            if book_id not in self.__books: # (check if book exists)
                raise BookNotFound(f"book ID '{book_id}' not found!")
            book = self.__books[book_id]

            if not book.is_available: # (check if already borrowed by someone)
                raise AlreadyBorrowed(f"'{book.title}' is already borrowed!")

            if len(user.borrowed) >= user.borrow_limit: # (check if user reached their limit)
                print(f"{user.name} has reached the limit of {user.borrow_limit} books!")
                return

            # all checks passed - borrow the book
            book.is_available = False
            user.borrowed.append(book_id)
            logging.info(f"Book borrowed: {book.title} by {user.name}")
            print(f"'{book.title}' borrowed by {user.name}!")

        except BookNotFound as e:
            logging.error(f"Book ID not found: {book_id}")
            print(f"Error: {e}")

        except AlreadyBorrowed as e:
            logging.error(f"Book already borrowed: {book_id}")
            print(f"Error: {e}")

    def return_book(self, book_id, user): # returning a book
        try:
            if book_id not in self.__books: # (check if book exists)
                raise BookNotFound(f"book ID '{book_id}' not found!")

            if book_id not in user.borrowed: # (check if this user actually borrowed it)
                raise NotBorrowed(f"you haven't borrowed book ID '{book_id}'!")

            # all good - return it
            book = self.__books[book_id]
            book.is_available = True
            user.borrowed.remove(book_id)
            logging.info(f"Book returned: {book.title} by {user.name}")
            print(f"'{book.title}' returned successfully!")

        except BookNotFound as e:
            logging.error(f"Book ID not found during return: {book_id}")
            print(f"Error: {e}")

        except NotBorrowed as e:
            logging.error(f"Return failed - not borrowed: {book_id}")
            print(f"Error: {e}")
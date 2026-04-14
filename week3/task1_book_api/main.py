from fastapi import FastAPI

app = FastAPI() # creating the fastapi app

# sample list of books - will grow when we add more
books = [
    {"id": 1, "title": "Harry Potter", "author": "JK Rowling"},
    {"id": 2, "title": "Percy Jackson", "author": "Rick Riordan"},
    {"id": 3, "title": "The Alchemist", "author": "Paulo Coelho"},
]

@app.get("/") # GET / - welcome route
def home():
    return {"message": "Welcome to the Book API"}

@app.get("/books") # GET /books - returns all books in the list
def get_books():
    return {"books": books}

@app.post("/books") # POST /books - accepts a new book and adds it to the list
def add_book(book: dict):
    # giving it a new id based on list length
    book["id"] = len(books) + 1
    books.append(book)
    return {"message": "Book added!", "book": book}

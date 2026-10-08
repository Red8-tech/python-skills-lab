from book import Book
from dvd import DVD
from library import Library

book = Book(
    "Clean Code",
    "Robert C. Martin",
    "9780132350884"
)

dvd = DVD(
    "Inception",
    "Christopher Nolan",
    148
)

library = Library()

library.add_item(book)
library.add_item(dvd)

print("Library items:")
for item in library.list_items():
    print(item.title)

print("\nBorrowing Book:")
library.borrow_item("Clean Code")

print("\nBorrowing DVD:")
library.borrow_item("Inception")

print("\nReturning DVD:")
library.return_item("Inception")

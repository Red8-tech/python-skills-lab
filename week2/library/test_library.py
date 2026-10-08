from book import Book
from library import Library


book1 = Book("Clean Code", "Robert C. Martin", "9780132350884")
book2 = Book("Python Crash Course", "Eric Matthes", "9781718502703")
book3 = Book("The Pragmatic Programmer", "David Thomas", "9780135957059")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("All books:")
for book in library.list_books():
    print(book.title)

print("\nFinding book:")
found_book = library.find_book("9781718502703")

if found_book:
    print(found_book.title)


library.remove_book(book2)

print("\nAfter removing book2:")
for book in library.list_books():
    print(book.title)


print("\nBorrowing book:")
library.borrow_book("9780132350884")

print("Book available:", book1.is_available)

print("\nTrying to borrow the same book:")
library.borrow_book("9780132350884")

print("\nReturning book:")
library.return_book("9780132350884")

print("Book available:", book1.is_available)

print("\nTrying to return it again:")
library.return_book("9780132350884")

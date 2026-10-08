from book import Book

book1 = Book(
    "Clean Code",
    "Robert C. Martin",
    "9780132350884"
)

print(book1.title)
print(book1.author)
print(book1.isbn)
print(book1.is_available)

book1.borrow()

print(book1.is_available)

book1.return_item()

print(book1.is_available)

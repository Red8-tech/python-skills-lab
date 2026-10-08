class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"


book = Book(
    "Clean Code",
    "Robert C. Martin",
    "9780132350884"
)

print(book)

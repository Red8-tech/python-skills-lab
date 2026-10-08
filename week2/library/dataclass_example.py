from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str


book1 = Book("Clean Code", "Robert C. Martin", "9780132350884")
book2 = Book("Clean Code", "Robert C. Martin", "9780132350884")

print(book1)
print(book2)
print(book1 == book2)

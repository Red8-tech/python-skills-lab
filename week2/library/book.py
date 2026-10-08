from library_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def borrow(self):
        self.is_available = False
        print(f"'{self.title}' has been borrowed.")

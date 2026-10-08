class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def borrow(self):
        self.is_available = False

    def return_item(self):
        self.is_available = True

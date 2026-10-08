from library_item import LibraryItem


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration

    def borrow(self):
        self.is_available = False
        print(f"'{self.title}' has been borrowed for 7 days.")

from library_item import LibraryItem


class Library:
    def __init__(self):
        self.items = []


    def add_item(self, item: LibraryItem):
        self.items.append(item)


    def remove_item(self, item: LibraryItem):
        if item in self.items:
            self.items.remove(item)


    def list_items(self):
        return self.items


    def find_item(self, title: str):
        for item in self.items:
            if item.title == title:
                return item
        return None


    def borrow_item(self, title: str):
        item = self.find_item(title)

        if item is None:
            print("Item not found!")
            return

        if not item.is_available:
            print("Item is already borrowed.")
            return

        item.borrow()


    def return_item(self, title: str):
        item = self.find_item(title)

        if item is None:
            print("Item not found!")
            return

        if item.is_available:
            print("Item is already available.")
            return

        item.return_item()
        print(f"'{item.title}' has been returned.")

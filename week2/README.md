# Week 2 — Object-Oriented Python

This folder contains my Week 2 practice for **Object-Oriented Programming (OOP) in Python**.

The focus of this week was learning how to design classes, manage object state, use inheritance and polymorphism, and understand when to use inheritance versus composition.

---

## Topics Covered

- Classes and Objects
- Attributes and Methods
- Constructors and `self`
- Encapsulation
- Class Responsibilities
- Inheritance
- `super()`
- Method Overriding
- Polymorphism
- Composition
- Dataclasses
- Properties
- Property Setters
- `__repr__()`
- Inheritance vs Composition
- Basic OOP Design

---

## Project 1 — Library Management System

The main practical exercise was a small library management system.

### Project Structure

```text
week2/
└── library/
    ├── book.py
    ├── dvd.py
    ├── library_item.py
    ├── library.py
    ├── test_book.py
    ├── test_dvd.py
    ├── test_library.py
    ├── test_polymorphism.py
    ├── dataclass_example.py
    ├── property_example.py
    └── repr_example.py
```

---

## 1. Classes and Objects

Started with a `Book` class containing:

- `title`
- `author`
- `isbn`
- `is_available`

Methods:

```python
borrow()
return_book()
```

Learned that a **class** defines the structure and behavior, while an **object** is an instance of that class.

Example:

```python
book1 = Book(
    "Clean Code",
    "Robert C. Martin",
    "9780132350884"
)
```

Multiple objects maintain their own independent state.

---

## 2. Library Class

Created a `Library` class responsible for managing multiple books/items.

Responsibilities included:

```python
add_item()
remove_item()
list_items()
find_item()
borrow_item()
return_item()
```

This introduced the idea of **separation of responsibilities**.

The `Book` class manages the state and behavior of an individual book, while the `Library` class manages a collection of library items.

---

## 3. Inheritance

Created a common parent class:

```python
class LibraryItem:
    ...
```

Both `Book` and `DVD` inherit from it:

```text
             LibraryItem
                 │
          ┌──────┴──────┐
          ▼             ▼
        Book            DVD
```

The common parent provides:

- `title`
- `is_available`
- `borrow()`
- `return_item()`

This avoids duplicating common functionality.

---

## 4. `super()`

Used:

```python
super().__init__(title)
```

to call the constructor of the parent class.

For example:

```python
class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn
```

This allows the parent class to initialize the common attributes while the child class handles its own specific attributes.

---

## 5. Method Overriding

The `DVD` class overrides the `borrow()` method.

```python
class DVD(LibraryItem):
    def borrow(self):
        self.is_available = False
        print(f"'{self.title}' has been borrowed for 7 days.")
```

The parent provides generic behavior, while the child provides specialized behavior.

---

## 6. Polymorphism

The `Library` works with `LibraryItem` objects without needing to know whether an object is a `Book` or a `DVD`.

For example:

```python
item.borrow()
```

can result in different behavior depending on the object's actual type.

```text
Book
 └── borrow()
      → 'Clean Code' has been borrowed.

DVD
 └── borrow()
      → 'Inception' has been borrowed for 7 days.
```

This demonstrated **polymorphism**.

---

## 7. Composition

The `Library` contains library items:

```python
class Library:
    def __init__(self):
        self.items = []
```

The library therefore **HAS-A** collection of library items.

This is composition.

```text
Library
   │
   └── HAS-A → collection of LibraryItems
```

---

## 8. Dataclasses

Practiced Python's `dataclass` feature:

```python
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    isbn: str
```

Dataclasses automatically generate useful methods such as:

- `__init__()`
- `__repr__()`
- `__eq__()`

Example output:

```text
Book(title='Clean Code', author='Robert C. Martin', isbn='9780132350884')
```

Dataclasses are particularly useful for classes that primarily store data.

---

## 9. Properties

Created a `BankAccount` example to understand controlled attribute access.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = value
```

This prevents invalid state such as:

```python
account.balance = -500
```

and raises:

```text
ValueError: Balance cannot be negative.
```

This demonstrated **encapsulation using properties**.

---

## 10. `__repr__()`

Implemented a custom `__repr__()` method:

```python
def __repr__(self):
    return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
```

This provides a useful developer-friendly representation of an object.

Instead of:

```text
<__main__.Book object at 0x...>
```

we can get:

```text
Book(title='Clean Code', author='Robert C. Martin', isbn='9780132350884')
```

---

## Inheritance vs Composition

One of the main design lessons from this week was understanding when inheritance should and should not be used.

### IS-A → Inheritance

```text
Book IS-A LibraryItem
DVD  IS-A LibraryItem
```

This is appropriate for inheritance.

### HAS-A → Composition

```text
Book HAS-A Author
Book HAS-A Publisher
Library HAS-A LibraryItems
```

These relationships are better represented using composition.

### General Rule

> **Inheritance represents an IS-A relationship.**

> **Composition represents a HAS-A relationship.**

Inheritance should not be used simply to reuse code. There should be a genuine conceptual relationship between the parent and child classes.

---

## Key OOP Concepts Learned

| Concept | Example |
|---|---|
| Class | `Book`, `Library`, `DVD` |
| Object | `book1`, `dvd` |
| Attribute | `title`, `isbn` |
| Method | `borrow()`, `return_item()` |
| Constructor | `__init__()` |
| Encapsulation | `BankAccount.balance` |
| Inheritance | `Book(LibraryItem)` |
| `super()` | `super().__init__(title)` |
| Method Overriding | `DVD.borrow()` |
| Polymorphism | `item.borrow()` |
| Composition | `Library` contains items |
| Dataclass | `@dataclass` |
| Property | `@property` |
| Setter | `@balance.setter` |
| Representation | `__repr__()` |

---

## Verification

The following exercises were successfully executed:

### Book

```text
Clean Code
Robert C. Martin
9780132350884
True
False
True
```

### DVD

```text
Inception
Christopher Nolan
148
True
'Inception' has been borrowed for 7 days.
False
True
```

### Polymorphism

```text
Library items:
Clean Code
Inception

Borrowing Book:
'Clean Code' has been borrowed.

Borrowing DVD:
'Inception' has been borrowed for 7 days.

Returning DVD:
'Inception' has been returned.
```

### Property validation

```text
5000
10000
ValueError: Balance cannot be negative.
```

### Custom `__repr__`

```text
Book(title='Clean Code', author='Robert C. Martin', isbn='9780132350884')
```

---

## Pending Exercises

The following practical exercises are planned but not yet completed:

### 1. Parking Lot

Practice:

- Classes
- Object state
- Composition
- Class responsibilities

### 2. Bank Account

Practice:

- Encapsulation
- Properties
- Validation
- State management

### 3. Playlist

Practice:

- Classes
- Collections
- Methods
- Object relationships

These will be completed as **timed design exercises** to test the ability to independently design small class hierarchies.

---

## Week 2 Learning Outcome

By the end of the completed portion of Week 2, I can:

- Create classes and objects in Python
- Design attributes and methods
- Separate responsibilities between classes
- Build basic class hierarchies
- Use inheritance and `super()`
- Override methods
- Explain and implement polymorphism
- Use composition
- Create dataclasses
- Use properties and setters for validation
- Implement `__repr__()`
- Explain the difference between inheritance and composition
- Identify when inheritance should **not** be used

---

## Next Step

Complete the three timed OOP exercises:

```text
Parking Lot
     ↓
Bank Account
     ↓
Playlist
```

Then complete the final Week 2 goal:

> **Design a small class hierarchy independently and explain when composition is preferable to inheritance.**

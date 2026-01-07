from abc import ABC, abstractmethod

class Book(ABC):
    """
    Abstract base class for all books in the library.
    """

    def __init__(self, book_id, title, author):
        self._id = book_id
        self._title = title
        self._author = author

    @abstractmethod
    def borrow(self):
        """Borrow the book."""
        pass

    @abstractmethod
    def return_book(self):
        """Return the book."""
        pass

    @abstractmethod
    def to_dict(self):
        """Convert book to dictionary."""
        pass

    def __str__(self):
        return f"{self._title} by {self._author}"

    def __eq__(self, other):
        return isinstance(other, Book) and self._id == other._id

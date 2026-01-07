from .book import Book
from .exceptions import BookNotAvailableError

class PhysicalBook(Book):
    """
    Represents a physical book with limited copies.
    """

    def __init__(self, book_id, title, author, available_copies):
        super().__init__(book_id, title, author)
        self._available_copies = available_copies

    def borrow(self):
        if self._available_copies <= 0:
            raise BookNotAvailableError("No copies available.")
        self._available_copies -= 1

    def return_book(self):
        self._available_copies += 1

    def to_dict(self):
        return {
            "type": "physical",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "available_copies": self._available_copies
        }

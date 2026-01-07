from .book import Book

class EBook(Book):
    """
    Represents an electronic book.
    """

    def __init__(self, book_id, title, author, file_size_mb):
        super().__init__(book_id, title, author)
        self._file_size_mb = file_size_mb

    def borrow(self):
        pass  # unlimited access

    def return_book(self):
        pass

    def to_dict(self):
        return {
            "type": "ebook",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "file_size_mb": self._file_size_mb
        }

class Member:
    """
    Represents a library member.
    """

    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book. Cannot borrow the same book twice."""
        if book in self._borrowed_books:
            raise ValueError("Book already borrowed.")
        self._borrowed_books.append(book)

    def return_book(self, book):
        """Return a book. Cannot return books not borrowed."""
        if book not in self._borrowed_books:
            raise ValueError("Book not borrowed.")
        self._borrowed_books.remove(book)

    def to_dict(self):
        """Convert member to dictionary (for JSON)."""
        return {
            "id": self._member_id,
            "name": self._name,
            "borrowed_books": [b._id for b in self._borrowed_books]
        }

    def __str__(self):
        return f"{self._name} (ID: {self._member_id})"

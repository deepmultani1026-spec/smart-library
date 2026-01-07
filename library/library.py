import json
from .loan import Loan
from .exceptions import *
from .physical_book import PhysicalBook
from .ebook import EBook
from .member import Member

class Library:
    """
    Main system controller for the library.
    """

    def __init__(self):
        self._books = {}     # book_id -> Book object
        self._members = {}   # member_id -> Member object
        self._loans = []     # list of Loan objects

    def add_book(self, book):
        self._books[book._id] = book

    def add_member(self, member):
        self._members[member._member_id] = member

    def borrow_book(self, member_id, book_id):
        if member_id not in self._members:
            raise MemberNotFoundError()
        if book_id not in self._books:
            raise BookNotFoundError()

        book = self._books[book_id]
        member = self._members[member_id]

        book.borrow()          # can raise BookNotAvailableError
        member.borrow_book(book)

        self._loans.append(Loan(book, member))

    def return_book(self, member_id, book_id):
        book = self._books[book_id]
        member = self._members[member_id]

        member.return_book(book)
        book.return_book()

    def save_to_file(self, filename):
        """Save all books, members, and loans to a JSON file."""
        data = {
            "books": [b.to_dict() for b in self._books.values()],
            "members": [m.to_dict() for m in self._members.values()],
            "loans": [l.to_dict() for l in self._loans]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        """Load books and members from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)

        # Reset current data
        self.__init__()

        # Recreate books
        for b in data.get("books", []):
            if b["type"] == "physical":
                self.add_book(PhysicalBook(b["id"], b["title"], b["author"], b["available_copies"]))
            else:
                self.add_book(EBook(b["id"], b["title"], b["author"], b["file_size_mb"]))

        # Recreate members
        for m in data.get("members", []):
            self.add_member(Member(m["id"], m["name"]))

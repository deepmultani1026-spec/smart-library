from datetime import date

class Loan:
    """
    Represents a borrowing transaction.
    """

    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.date_borrowed = date.today().isoformat()

    def to_dict(self):
        """Convert loan to dictionary for JSON."""
        return {
            "book_id": self.book._id,
            "member_id": self.member._member_id,
            "date": self.date_borrowed
        }

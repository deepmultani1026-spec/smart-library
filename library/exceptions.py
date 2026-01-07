class BookNotAvailableError(Exception):
    """Raised when a physical book has no copies left to borrow."""
    pass

class BookNotFoundError(Exception):
    """Raised when a book ID is not found in the library."""
    pass

class MemberNotFoundError(Exception):
    """Raised when a member ID is not found in the library."""
    pass

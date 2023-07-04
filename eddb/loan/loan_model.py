from datetime import datetime,timezone
from dataclasses import dataclass, field
from eddb.util.util import str_uuid4

@dataclass
class Loan:
    """
    Class representing when a student picks a book from the library
    This is a data class, only method implemented is the special method
    __dict__ for json representation
    """

    id: str = field(default_factory=str_uuid4)
    book_id: str = "Book"
    student_id: str = "Unknown"
    loan_date: datetime = field(default_factory=datetime.now(timezone.utc))
    payday: datetime = None
    status: str = "inactive"

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "book_id":f"{self.book_id}",
            "student_id":f"{self.student_id}",
            "loan_date":f"{self.loan_date}",
            "payday":f"{self.payday}",
            "status":f"{self.status}",
        }

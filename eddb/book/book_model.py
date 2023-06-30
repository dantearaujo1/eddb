from dataclasses import dataclass, field
from eddb.util.util import str_uuid4

@dataclass
class Book:
    """DocString"""

    id: str = field(default_factory=str_uuid4)
    title: str = "Book"
    author: str = "Unknown"

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "title":f"{self.title}",
            "author":f"{self.author}",
        }

from dataclasses import dataclass, field
from eddb.util.util import str_uuid4

@dataclass
class Book:
    """Book dataclass that has only 3 attributes"""

    id: str = field(default_factory=str_uuid4)
    title: str = "Book"
    author: str = "unknown"

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "title":f"{self.title}",
            "author":f"{self.author}",
        }

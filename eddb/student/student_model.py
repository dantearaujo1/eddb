from dataclasses import dataclass, field
from eddb.util.util import str_uuid4

@dataclass
class Student:
    """docstring"""

    id: int = 0
    name: str = "unknown"
    surname: str = "unknown"
    email: str = ""

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "name":f"{self.name}",
            "surname":f"{self.surname}",
            "email":f"{self.email}",
        }


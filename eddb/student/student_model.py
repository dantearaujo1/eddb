import uuid
from dataclasses import dataclass, field
from util.util import str_uuid4


@dataclass
class Student:
    """DocString"""

    id: int = 0
    name: str = "User"
    surname: str = ""
    
    def __dict__(self):
        return {
            "id":f"{self.id}",
            "name":f"{self.name}",
            "surname":f"{self.surname}"
        }

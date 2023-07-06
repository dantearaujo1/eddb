from random import random
from dataclasses import dataclass, field
from eddb.util.util import str_uuid4

@dataclass
class Student:
    """Student dataclass that has only 4 attributes"""

    id: int = int(random()*100000)
    name: str = "unknown"
    surname: str = "unknown"
    email: str = ""

    def __dict__(self):
        return {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            "email":self.email
        }


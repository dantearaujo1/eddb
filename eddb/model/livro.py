import uuid
from dataclasses import dataclass, field

@dataclass
class Livro:
    id: [] = field(default_factory=uuid.uuid4)
    nome: str = ""
    autor: str = ""

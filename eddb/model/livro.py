import uuid
from dataclasses import dataclass

@dataclass
class Livro:
    uuid: str = str(uuid.uuid4())
    nome: str = ""
    autor: str = ""

import uuid
from dataclasses import dataclass, field
from util.util import str_uuid4


@dataclass
class Livro:
    id: str = field(default_factory=str_uuid4)
    nome: str = ""
    autor: str = ""

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "titulo":f"{self.nome}",
            "autor":f"{self.autor}",
        }

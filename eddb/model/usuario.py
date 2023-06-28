import uuid
from dataclasses import dataclass, field
from util.util import str_uuid4


@dataclass
class Usuario:
    """DocString"""

    id: str = field(default_factory=str_uuid4)
    nome: str = "User"
    sobrenome: str = ""
    matricula: int = 0

    def __dict__(self):
        return {
            "id":f"{self.id}",
            "nome":f"{self.nome}",
            "sobrenome":f"{self.sobrenome}",
            "matrícula":self.sobrenome,
        }

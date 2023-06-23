import uuid
import datetime
from dataclasses import dataclass
from .usuario import Usuario
from .livro import Livro

@dataclass
class Emprestimo:
    uuid: str = str(uuid.uuid4())
    livro: Livro = None
    usuario: Usuario = None
    status: str = "Ativo"
    data: datetime.datetime = datetime.datetime.now()

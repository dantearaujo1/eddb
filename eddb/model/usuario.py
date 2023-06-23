import uuid
from dataclasses import dataclass


@dataclass
class Usuario:
    """DocString"""

    uuid: str = str(uuid.uuid4())
    nome: str = ""


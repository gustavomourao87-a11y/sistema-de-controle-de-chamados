from pydantic import BaseModel
from typing import Literal

class Chamado(BaseModel):
    nome: str
    descricao: str
    categoria: str
class ChamadoStatus(BaseModel):
    status: Literal["Aberto", "Em andamento", "Concluído"]
class ChamadoResposta(BaseModel):
    id: int
    nome: str
    descricao: str
    categoria: str
    status: str
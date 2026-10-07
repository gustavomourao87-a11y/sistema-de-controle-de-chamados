from pydantic import BaseModel, Field, field_validator  
from typing import Literal

class Chamado(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    descricao: str = Field(..., min_length=1, max_length=500)
    categoria: Literal["Suporte", "Desenvolvimento", "Administração"]
class ChamadoStatus(BaseModel):
    status: Literal["Aberto", "Em andamento", "Concluído"]
class ChamadoResposta(BaseModel):
    id: int
    nome: str
    descricao: str
    categoria: str
    status: str

@field_validator("nome")
def validar_nome(cls, value):
    value = value.strip()

    if not value:
        raise ValueError("O nome não pode estar vazio.")
    
    return value

@field_validator("descricao")
def validar_descricao(cls, value):
    value = value.strip()

    if not value:
        raise ValueError("A descrição não pode estar vazia.")
    
    return value

@field_validator("categoria", mode="before")
def validar_categoria(cls, value):
    value = value.strip()
    
    if not value:
        raise ValueError("A categoria não pode estar vazia.")
    return value
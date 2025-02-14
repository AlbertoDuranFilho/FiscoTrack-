from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Schema para Obrigacao Acessória (entrada/saída de dados)
class ObrigacaoAcessoria(BaseModel):
    nome: str
    periodicidade: str  # Mensal, trimestral, anual

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoria):
    empresa_id: int

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoria):
    id: int
    empresa_id: int

    class Config:
        from_attributes = True

# Schema para Empresa (entrada/saída de dados)
class Empresa(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(Empresa):
    pass  # Usado para criacao de empresa

class EmpresaResponse(Empresa):
    id: int
    obrigacoes: List[ObrigacaoAcessoriaResponse] = []

    class Config:
        from_attributes = True

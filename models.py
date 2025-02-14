from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Modelo da Empresa
class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cnpj = Column(String, unique=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

# Modelo da Obrigacao Acessória
class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)  # Mensal, trimestral, anual
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="obrigacoes")

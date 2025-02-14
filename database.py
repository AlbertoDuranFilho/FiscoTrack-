from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do .env
load_dotenv(encoding="utf-8")

# Pegar as credenciais do banco de dados do .env
DATABASE_URL = os.getenv("DB_URL")

# Criar a conexão com o banco de dados
db = create_engine(DATABASE_URL)

# Criar a sessão do banco
SessionLocal = sessionmaker(db)

# Base para os modelos
Base = declarative_base()

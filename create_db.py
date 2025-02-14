from database import db, Base
import models
import os
import dotenv

# Carregar as variáveis de ambiente do .env
dotenv.load_dotenv(encoding="utf-8")

# Pegar as credenciais do banco de dados do .env
DATABASE_URL = os.getenv("DB_URL")

# Criar todas as tabelas no banco de dados
print("Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=db)
print("Tabelas criadas com sucesso!")

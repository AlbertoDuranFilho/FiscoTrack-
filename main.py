from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, db
import models, schemas

#Criar as tebelas no banco de dados
models.Base.metadata.create_all(bind=db)

#Criar a aplicação FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota raiz
@app.get("/")
def root():
    return {"message": "API está rodando!"}

# Endpoints para Empresa
@app.post("/empresa/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresa/", response_model=list[schemas.Empresa])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

@app.get("/empresa/{empresa_id}", response_model=schemas.Empresa)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.put("/empresa/{empresa_id}", response_model=schemas.Empresa)
def update_empresa(empresa_id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    for key, value in empresa.dict().items():
        setattr(db_empresa, key, value)

    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresa/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    db.delete(db_empresa)
    db.commit()
    return {"message": "Empresa deletada com sucesso"}

# ----------------------- Endpoints para Obrigação Acessória -----------------------
@app.post("/obrigacao_acessoria/", response_model=schemas.ObrigacaoAcessoria, status_code=201)
def create_obrigacao_acessoria(obrigacao_acessoria: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = models.ObrigacaoAcessoria(**obrigacao_acessoria.model_dump())
    db.add(db_obrigacao_acessoria)
    db.commit()
    db.refresh(db_obrigacao_acessoria)
    return db_obrigacao_acessoria

@app.get("/obrigacao_acessoria/", response_model=list[schemas.ObrigacaoAcessoria])
def listar_obrigacoes_acessorias(db: Session = Depends(get_db)):
    return db.query(models.ObrigacaoAcessoria).all()

@app.get("/obrigacao_acessoria/{obrigacao_acessoria_id}", response_model=schemas.ObrigacaoAcessoria)
def obter_obrigacao_acessoria(obrigacao_acessoria_id: int, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()
    if db_obrigacao_acessoria is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return db_obrigacao_acessoria

@app.put("/obrigacao_acessoria/{obrigacao_acessoria_id}", response_model=schemas.ObrigacaoAcessoria)
def update_obrigacao_acessoria(obrigacao_acessoria_id: int, obrigacao_acessoria: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()
    if db_obrigacao_acessoria is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    
    for key, value in obrigacao_acessoria.dict().items():
        setattr(db_obrigacao_acessoria, key, value)

    db.commit()
    db.refresh(db_obrigacao_acessoria)
    return db_obrigacao_acessoria

@app.delete("/obrigacao_acessoria/{obrigacao_acessoria_id}")
def delete_obrigacao_acessoria(obrigacao_acessoria_id: int, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()
    if db_obrigacao_acessoria is None:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    
    db.delete(db_obrigacao_acessoria)
    db.commit()
    return {"message": "Obrigação acessória deletada com sucesso"}
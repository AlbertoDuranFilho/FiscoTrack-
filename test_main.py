import pytest
from fastapi.testclient import TestClient
from main import app  # Importa a aplicação FastAPI

client = TestClient(app)  # Cliente de teste para fazer requisições

# ✅ Teste 1: Verifica se a API está rodando
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API está rodando!"}

# ✅ Teste 2: Criar uma nova empresa
def test_get_empresa():
    # Criar uma empresa antes do teste
    data = {
        "nome": "Empresa Teste",
        "cnpj": "12345678000199",
        "endereco": "Rua Teste, 123",
        "email": "teste@empresa.com",
        "telefone": "11999999999"
    }
    create_response = client.post("/empresas/", json=data)
    empresa_id = create_response.json()["id"]  # Captura o ID criado

    # Agora tentamos buscar a empresa recém-criada
    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    assert response.json()["id"] == empresa_id

# ✅ Teste 3: Listar todas as empresas
def test_list_empresas():
    response = client.get("/empresa/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ✅ Teste 4: Buscar empresa por ID (assumindo que a empresa 1 já exista)
def test_get_empresa():
    response = client.get("/empresa/1")
    assert response.status_code in [200, 404]  # Pode ser sucesso ou erro caso não exista

# ✅ Teste 5: Criar uma nova obrigação acessória para uma empresa
def test_create_obrigacao():
    data = {
        "nome": "TESTE",
        "periodicidade": "mensal",
        "empresa_id": 2  # Assumindo que a empresa de ID 1 já existe
    }
    response = client.post("/obrigacao_acessoria/", json=data)
    assert response.status_code == 201
    assert response.json()["nome"] == "TESTE"

# ✅ Teste 6: Listar todas as obrigações acessórias
def test_list_obrigacoes():
    response = client.get("/obrigacao_acessoria/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ✅ Teste 7: Buscar uma obrigação acessória por ID
def test_get_obrigacao():
    response = client.get("/obrigacao_acessoria/1")  # Assumindo que a obrigação de ID 1 exista
    assert response.status_code in [200, 404]

from fastapi.testclient import TestClient
from main import app

# Criamos um "cliente falso" que simula um navegador acessando nossa API
client = TestClient(app)

def test_root_not_found():
    """Testa se a raiz retorna 404 (já que não definimos rota na raiz /)"""
    response = client.get("/")
    assert response.status_code == 404

def test_triagem_fluxo_padrao():
    """
    Testa o 'Caminho Feliz':
    Envia um sintoma válido e espera uma resposta 200 com a estrutura correta.
    """
    payload = {"description": "Estou com muita dor de cabeça e enjoo."}
    response = client.post("/triagem", json=payload)
    
    # 1. O status code tem que ser 200 (Sucesso)
    assert response.status_code == 200
    
    # 2. Vamos ler o JSON de resposta
    data = response.json()
    
    # 3. Verificamos se as chaves existem no JSON
    assert "sintoma" in data
    assert "categoria_sugerida" in data
    assert "confianca" in data
    
    # 4. Verificamos se o sintoma devolvido é o mesmo que enviamos
    assert data["sintoma"] == payload["description"]

def test_triagem_validacao_vazia():
    """
    Testa como a API reage se enviarmos um JSON errado.
    O Pydantic (do FastAPI) deve barrar e retornar erro 422 (Unprocessable Entity).
    """
    # Enviando um dicionário vazio, sem o campo 'description'
    response = client.post("/triagem", json={})
    
    assert response.status_code == 422
from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus

def test_read_root_deve_retornar_OK():
    client = TestClient(app)
    response = client.get("/")  # Captura a resposta da requisição
    assert response.status_code == HTTPStatus.ACCEPTED  # Verifica se o status é 200
    assert response.json() == {"Test": "Olá mundo !"}  # Verifica o conteúdo da resposta

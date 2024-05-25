from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá Mundo"}

def test_read_itens():
    response = client.get("/api/itens")
    assert response.status_code == 200
    assert response.json() == [{"item": "Item 1"}, {"item": "Item 2"}]

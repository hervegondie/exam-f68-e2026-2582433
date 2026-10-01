# tests/test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    """Fixture qui fournit un client HTTP asynchrone pour tester l'API."""
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as ac:
        yield ac

@pytest.mark.anyio
async def test_predict_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/predict", json={
        "features": [3.5, 1.2, 4.9]
    })
    assert resp.status_code == 200
    assert {"predictions": [7.0, 2.4, 9.8]} == resp.json()

@pytest.mark.anyio
async def test_predict_unprocessable_entity():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/predict", json={
        "feature1": 3.5,
        "feature2": 1.2,
        "feature3": 4.9
    })
    assert resp.status_code == 422
    
    
# Tests D'integration
@pytest.mark.anyio
async def test_predict_integration_features_vide(client):
    """
    Test d'intégration : vérifie que l'API renvoie une liste de prédictions vide 
    lorsque la liste de features fournie est vide.
    """
    payload = {
        "features": []
    }
    
    response = await client.post("/predict", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "predictions" in data  
    assert data["predictions"] == []

@pytest.mark.anyio
async def test_predict_integration_features_negatif(client):
    """
    Test d'intégration : vérifie que l'API gère correctement 
    les valeurs de features négatives.
    """
    payload = {
        "features": [-2.0, -4.5, -10.0]
    }
    
    response = await client.post("/predict", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "predictions" in data
    assert isinstance(data["predictions"], list)
    assert len(data["predictions"]) > 0
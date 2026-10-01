import pytest
from pydantic import ValidationError
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.main import predict_endpoint, PredictionRequest

@pytest.fixture
async def client():
    """Fixture qui fournit un client HTTP asynchrone pour tester l'API."""
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as ac:
        yield ac

@pytest.mark.anyio
def test_predict_success_basic():
    data = PredictionRequest(features=[3.5, 1.2, 4.9])
    resp = predict_endpoint(data)
    assert resp == {"predictions": [7.0, 2.4, 9.8]}


@pytest.mark.anyio
def test_predict_success_string():
    data = PredictionRequest(features=["3.5", "1.2", "4.9"])
    resp = predict_endpoint(data)
    assert resp == {"predictions": [7.0, 2.4, 9.8]}

@pytest.mark.anyio
def test_predict_invalid_data ():
    with pytest.raises(ValidationError):
        PredictionRequest(features=["a", "b", "c"])
        
#Test unitaire - Liste vide
@pytest.mark.anyio
async def test_predict_success_features_vide(client):
    """
    Vérification du comportement de predict_endpoint avec une liste de features vide.
    """
    payload = {
        "features": []
    }
    response = await client.post("/predict", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "predictions" in data  
    assert data["predictions"] == []

# Test unitaire - Valeurs négatives
@pytest.mark.anyio
async def test_predict_success_features_negatif(client):
    """
    Vérifie le comportement de predict_endpoint avec des valeurs de features négatives.
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
    
    response = await client.post("/predict", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "predictions" in data  
    assert isinstance(data["predictions"], list)
    assert len(data["predictions"]) > 0
    
    
    
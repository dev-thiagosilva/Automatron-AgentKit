from src.agent_api.api import app as api_app
from fastapi.testclient import TestClient

client = TestClient(api_app)

def test_chat_endpoint():
    payload = [{"content": "Hello"}]
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    # The mock graph currently echoes the message prefixed with 'Researcher found info about:'
    assert data["response"].startswith("Researcher")

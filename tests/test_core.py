from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_another():
    response = client.get('/another')
    assert response.status_code == 200
    assert response.json() == { "messgae": "Hello another"}

def test_post_method():
    response = client.post('/post-method')
    assert response.status_code == 200
    assert response.json() == { "message": "Hello post-method"}
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict(client):
    response = client.post('/predict', data=dict(area='2000'))
    assert response.status_code == 200
    assert b'Price of House will be Rs. 3000000' in response.data

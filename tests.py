import pytest
import json
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_employees(client):
    response = client.get('/api/v1/employees')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['id'] == 1
    assert data[0]['firstName'] == 'John'
    assert data[0]['lastName'] == 'Doe'
    assert data[0]['emailId'] == 'john.doe@example.com'
    assert data[1]['id'] == 2
    assert data[1]['firstName'] == 'Jane'
    assert data[1]['lastName'] == 'Doe'
    assert data[1]['emailId'] == 'jane.doe@example.com'

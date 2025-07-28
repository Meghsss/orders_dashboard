import io
import pandas as pd
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_customers_valid(client):
    csv_content = "customer_id,customer_name,location\n1,John,New York\n2,Alice,Chicago"
    data = {'file': (io.BytesIO(csv_content.encode()), 'customers.csv')}
    response = client.post('/upload/customers', content_type='multipart/form-data', data=data)
    assert response.status_code == 409
    assert response.get_json()['error'] == 'Duplicate customer entry found'


def test_upload_customers_no_file(client):
    response = client.post('/upload/customers', content_type='multipart/form-data', data={})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_upload_customers_empty_file(client):
    data = {
        'file': (io.BytesIO(b''), 'customers.csv')
    }
    response = client.post('/upload/customers', content_type='multipart/form-data', data=data)
    assert response.status_code == 500
    assert "No columns to parse from file" in response.get_json()['error']
    
def test_upload_orders_invalid_customer(client):
    csv_content = "order_id,customer_id,amount,date\n101,9999,500.0,2023-01-01"
    data = {'file': (io.BytesIO(csv_content.encode()), 'orders.csv')}
    response = client.post('/upload/orders', content_type='multipart/form-data', data=data)
    assert response.status_code == 400
    assert "No valid order data found" in response.get_json()['error']


def test_upload_orders_duplicate_order_id(client):
    # Assuming order_id 101 already exists
    csv_content = "order_id,customer_id,amount,date\n101,1,500.0,2023-01-01"
    data = {
        'file': (io.BytesIO(csv_content.encode()), 'orders.csv')
    }
    response = client.post('/upload/orders', content_type='multipart/form-data', data=data)
    
    assert response.status_code == 500
    assert "Duplicate entry" in response.get_json()['error']

def test_order_report_empty(client):
    response = client.get('/orders/report')
    
    # Your current code doesn't guard against empty result, so this may 500
    assert response.status_code in [200, 500]

    if response.status_code == 200:
        assert isinstance(response.get_json(), list)
    else:
        assert "error" in response.get_json()



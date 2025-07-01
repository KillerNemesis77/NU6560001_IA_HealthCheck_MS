from flask import Flask, jsonify
import pytest

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check_acceptance(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
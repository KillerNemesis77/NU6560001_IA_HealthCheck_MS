import requests

def test_health_check_e2e():
    # Asume que el microservicio está corriendo en localhost:5000
    response = requests.get("http://localhost:5000/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
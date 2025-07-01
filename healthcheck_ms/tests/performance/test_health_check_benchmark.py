from app.main import create_app

def test_health_check_benchmark(benchmark):
    app = create_app()
    client = app.test_client()

    @benchmark
    def _():
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json() == {"status": "healthy"}
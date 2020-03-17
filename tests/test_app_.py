class Test_app:
    """Test app"""
    def test_app_returns_hello_world(self, client):
        response = client.get('/')
        assert response.status_code == 200
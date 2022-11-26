from flask.testing import FlaskClient

class TestMain:
    def test_root_status(self, test_client: FlaskClient):
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус кода неверный"

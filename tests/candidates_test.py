import pytest
from flask.testing import FlaskClient

class TestCandidates:
    def test_get_root_page(self, test_client: FlaskClient):
        response = test_client.get('/candidates/')

        assert response.status_code == 200, 'статус код response не 200'
    
    def test_single_candidate_page(self, test_client: FlaskClient):
        response = test_client.get('/candidates/1/')

        assert response.status_code == 200, 'статуc код response не 200'
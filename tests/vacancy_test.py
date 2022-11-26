import pytest
from flask.testing import FlaskClient


class TestVacancies:
    def test_get_vacancies_list(self, test_client: FlaskClient) -> None:
        response = test_client.get('/vacancies/')

        assert response.status_code == 200, "Ошибка статус коде в списоке вакансий"

    def test_get_vacancy(self, test_client: FlaskClient) -> None:
        response = test_client.get('/vacancies/1/')

        assert response.status_code == 200, "Ошибка статус коде в вакансии"

    def test_get_vacancy_with_unexist_id(self, test_client: FlaskClient) -> None:
        response = test_client.get('/vacancies/10000/')

        assert response.status_code == 200, "Ошибка должен вернуться 200"

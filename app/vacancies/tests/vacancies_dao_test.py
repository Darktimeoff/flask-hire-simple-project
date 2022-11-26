import pytest
from vacancies.dao.vacancies_dao import VacanciesDao


@pytest.fixture(scope='module')
def vacancies_dao():
    return VacanciesDao('./data/vacancies.json')

keys_should_be = {"pk", "position", "company", "salary"}

class TestVacanciesDao:
    def test_get_all(self, vacancies_dao: VacanciesDao):
        vacancies = vacancies_dao.get_all()

        assert vacancies is not None, 'Нету информации о вакансиях'
        assert type(vacancies) is list, 'Не правильный тип у вакансиях'
        assert len(vacancies) > 1, 'Вакансии пустые'
        assert set(vacancies[0].keys()) == keys_should_be, 'Вакансиях не правильная структура'

    def test_get_by_pk(self, vacancies_dao: VacanciesDao):
        vacancy = vacancies_dao.get_by_pk(1)

        assert vacancy is not None,'Не найдена вакансия по айди 1'
        assert type(vacancy) is dict, 'Вакансия неправильного типа'
        assert set(vacancy.keys()) == keys_should_be, 'Вакансии не правильная структура'
import pytest
from candidates.dao.candidates_dao import CandidatesDao

@pytest.fixture(scope="module")
def candidates_dao():
    return CandidatesDao('./data/candidates.json') #ToDo rewrite on config

keys_should_be = {"pk", "name", "position"}

class TestCandidatesDao:

    def test_get_all(self, candidates_dao: CandidatesDao):
        candidates = candidates_dao.get_all()
        assert type(candidates) is list, 'возвращается не список'
        assert len(candidates) > 1, 'возращается пустой список'
        assert set(candidates[0].keys()) == keys_should_be, 'не содержит нужный полей'
    
    def test_get_by_id(self, candidates_dao: CandidatesDao):
        candidate = candidates_dao.get_by_pk(1)

        assert candidate is not None, 'Кандидат не найден с айди 1'
        assert(candidate['pk'] == 1), 'Возвращается не правильный кандидат'
        assert set(candidate.keys()) == keys_should_be, 'неверный структура у кандидата'
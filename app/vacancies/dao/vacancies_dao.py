from classes.dao import Dao


class VacanciesDao(Dao):
    def get_by_pk(self, pk):
        for v in self.get_all():
            if v['pk'] == pk:
                return v

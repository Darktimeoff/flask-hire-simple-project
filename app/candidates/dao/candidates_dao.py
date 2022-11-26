import json
import logging
from classes.dao import Dao


class CandidatesDao(Dao):
    def get_by_pk(self, pk) -> dict | None:
        for c in self.get_all():
            if c['pk'] == pk:
                return c

        return None

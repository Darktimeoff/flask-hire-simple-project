import json
import logging


class Dao:
    __path: str = None

    def __init__(self, path: str):
        if type(path) is not str:
            raise TypeError("path must be a string")

        if not path:
            raise ValueError('path arg not defined')

        self.__path = path

    def get_path(self):
        return self.__path

    def load_data(self) -> list[dict]:
        try:
            with open(self.__path, 'rt', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.exception(f'Could not find file: {self.__path}')
            raise FileNotFoundError
        except json.JSONDecodeError as e:
            logging.exception(f'Could not decode file: {self.__path}')
            raise json.JSONDecodeError(e.msg, e.doc, e.pos)

    def get_all(self):
        return self.load_data()

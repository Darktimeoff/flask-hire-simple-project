from flask import Flask
from dotenv import load_dotenv
from os import environ
from logging import basicConfig

from app.main.views import main_blueprint
from app.candidates.views import сandidates_blueprint
from app.vacancies.views import vacancies_blueprint

basicConfig(filename='basic.log')

app = Flask(__name__)
load_dotenv(override=True)

if environ.get('APP_CONFIG') == 'local':
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

app.register_blueprint(main_blueprint)
app.register_blueprint(сandidates_blueprint)
app.register_blueprint(vacancies_blueprint)

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', False))

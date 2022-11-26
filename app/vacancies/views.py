from flask import Blueprint, render_template, abort
from .dao.vacancies_dao import VacanciesDao
import logging

vacancies_blueprint = Blueprint(
    'vacancies', __name__,
    url_prefix='/vacancies', template_folder='templates'
)

vacancies_dao = VacanciesDao('./data/vacancies.json')


@vacancies_blueprint.errorhandler(404)
def error_400(e):
    return render_template('404.html')


@vacancies_blueprint.route('/')
def page_vacancies_list():
    print('vacancies_list')
    vacancies = vacancies_dao.get_all()
    return render_template('vacancies_list.html', vacancies=vacancies)


@vacancies_blueprint.route('/<int:id>/')
def page_vacancy(id):
    vacancy = vacancies_dao.get_by_pk(id)
    if not vacancy:
        logging.error(f'Could not find vacancy {id}')

        abort(404)

    return render_template('vacancy.html', vacancy=vacancy)

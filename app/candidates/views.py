from flask import Blueprint, render_template, abort
from .dao.candidates_dao import CandidatesDao
import logging

сandidates_blueprint = Blueprint(
    'сandidates', __name__, url_prefix='/candidates', template_folder='templates')

candidates_dao = CandidatesDao("./data/candidates.json")


@сandidates_blueprint.errorhandler(404)
def page_404(e):
    return render_template('404.html')


@сandidates_blueprint.route("/")
def page_candidates_all():
    candidates = candidates_dao.get_all()

    return render_template('candidates_list.html', candidates=candidates)


@сandidates_blueprint.route("/<int:id>/")
def page_candidate(id):
    candidate = candidates_dao.get_by_pk(id)

    if not candidate:
        logging.error(f'could not find candidate {id}')

        abort(404)

    return render_template('candidate.html', candidate=candidate)

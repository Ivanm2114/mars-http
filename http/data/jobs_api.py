import flask
from flask import jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=['id', 'team_leader',
                                    'job', 'work_size', 'collaborators',
                                    'start_date', 'end_date', 'is_finished'])
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<string:job_id>')
def get_job(job_id):
    db_sess = db_session.create_session()
    if job_id.isdigit():
        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        print(job)
        if not job:
            return jsonify({'error': 'Not found'})
        return jsonify(
            {
                'job':
                    [job.to_dict(only=['id', 'team_leader',
                                       'job', 'work_size', 'collaborators',
                                       'start_date', 'end_date', 'is_finished'])]
            }
        )
    return jsonify({'error': 'Not found'})

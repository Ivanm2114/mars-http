import flask
from flask import jsonify, request

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


@blueprint.route('/api/news', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})

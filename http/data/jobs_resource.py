import flask
from flask import jsonify, request
from flask_restful import reqparse, abort, Api, Resource

from . import db_session
from .jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify(
            {
                'job':
                    [job.to_dict(only=['id', 'team_leader',
                                       'job', 'work_size', 'collaborators',
                                       'start_date', 'is_finished'])]
            }
        )

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        args = parser.parse_args()
        if not request.json:
            return jsonify({'error': 'Empty request'})
        elif not all(key in args for key in
                     ['team_leader',
                      'job', 'work_size', 'collaborators', 'is_finished']):
            return jsonify({'error': 'Bad request'})
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=['id', 'team_leader',
                  'job', 'work_size', 'collaborators',
                  'start_date', 'is_finished']) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})

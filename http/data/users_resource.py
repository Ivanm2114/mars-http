import flask
from flask import jsonify, request
from flask_restful import reqparse, abort, Api, Resource

from . import db_session
from .users import User

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hometown', required=True)


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(
            {
                'user':
                    [user.to_dict(only=['id', 'surname',
                                        'name', 'age', 'position',
                                        'speciality', 'address', 'email', 'modified_date', 'hometown'])]
            }
        )

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        args = parser.parse_args()
        if not request.json:
            return jsonify({'error': 'Empty request'})
        elif not all(key in args for key in
                     ['surname',
                      'name', 'age', 'position',
                      'speciality', 'address', 'email', 'hometown']):
            return jsonify({'error': 'Bad request'})
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.position = args['position']
        user.speciality = args['speciality']
        user.address = args['address']
        user.email = args['email']
        user.hometown = args['hometown']
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=['id', 'surname',
                  'name', 'age', 'position',
                  'speciality', 'address', 'email', 'modified_date', 'hometown']) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            email=args['email'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            hometown=args['hometown']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})

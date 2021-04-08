import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=['id', 'surname',
                                    'name', 'age', 'position',
                                    'speciality', 'address', 'email', 'modified_date', 'hometown'])
                 for item in users]
        }
    )


@blueprint.route('/api/users/<string:user_id>')
def get_user(user_id):
    db_sess = db_session.create_session()
    if user_id.isdigit():
        user = db_sess.query(User).filter(User.id == user_id).first()
        if not user:
            return jsonify({'error': 'Not found'})
        return jsonify(
            {
                'user':
                    [user.to_dict(only=['id', 'surname',
                                        'name', 'age', 'position',
                                        'speciality', 'address', 'email', 'modified_date', 'hometown'])]
            }
        )
    return jsonify({'error': 'Not found'})


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname',
                  'name', 'age', 'position',
                  'speciality', 'address', 'email', 'hometown']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if db_sess.query(User).filter(User.id == request.json['id']).first():
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hometown=request.json['hometown']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname',
                  'name', 'age', 'position',
                  'speciality', 'address', 'email', 'hometown']):
        return jsonify({'error': 'Bad request'})
    if not user:
        return jsonify({'error': 'Not found'})
    user.surname = request.json['surname']
    user.name = request.json['name']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.email = request.json['email']
    user.hometown = request.json['hometown']
    db_sess.commit()
    return jsonify({'success': 'OK'})

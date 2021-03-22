from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


def main(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    for worker in db_sess.query(User).filter(User.speciality.notlike('%engineer%'),
                                             User.position.notlike("%engineer%"),
                                             User.address.like('module_1')).all():
        print(worker.id)


if __name__ == '__main__':
    main(input())

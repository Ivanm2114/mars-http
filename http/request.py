from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


def main(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    user = db_sess.query(User).filter(User.id == 3).first()
    user.set_password('4321')
    db_sess.commit()

    user = db_sess.query(User).filter(User.id == 1).first()
    user.set_password('1234')
    db_sess.commit()


if __name__ == '__main__':
    main('db/mars_explorer.db')

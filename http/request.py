from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

def main(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    user = db_sess.query(User).filter(User.address.like('%1'))
    for x in user:
        print(x)


if __name__ == '__main__':
    main(input())

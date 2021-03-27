from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department


def main(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    arr = []
    dep = db_sess.query(Department).filter(Department.id == 1).first()
    workers = [int(x) for x in dep.members.split(',')]
    for worker in workers:
        jobs = db_sess.query(Jobs).filter((Jobs.team_leader == worker) | Jobs.collaborators.like(f'%{worker}%')).all()
        if sum(list(x.work_size for x in jobs)) >= 25:
            user = db_sess.query(User).filter(User.id == worker).first()
            print(user.surname, user.name)


if __name__ == '__main__':
    main(input())

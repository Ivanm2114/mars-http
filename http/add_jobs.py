from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    job = Jobs()
    job.team_leader = 3
    job.job = 'Washing dishes'
    job.work_size = 15
    job.collaborators = '3,6'
    job.is_finished = False

    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()

from flask import Flask
from data import db_session
from data.departments import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    job = Department()
    job.chief = 2
    job.title = 'Cleaning deck'
    job.members = '2,3'
    job.email = 'idgaf'

    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()

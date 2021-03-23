from flask import Flask, request, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def f():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    works = []
    for job in db_sess.query(Jobs).all():
        work = [job.job, job.leader.surname + job.leader.name, str(job.work_size) + ' hours',
                job.collaborators, job.is_finished]
        works.append(work)
    return render_template('jobs.html', jobs=works)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000, host='127.0.0.1')

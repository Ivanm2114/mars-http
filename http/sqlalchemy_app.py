import datetime

from flask import Flask, request, render_template, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.utils import redirect

from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.user import RegisterForm, LoginForm
from forms.jobs import CreateJob, DeleteJob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def f():
    db_sess = db_session.create_session()
    works = []
    for job in db_sess.query(Jobs).all():
        work = [job.job, job.leader.surname + ' ' + job.leader.name, str(job.work_size) + ' hours',
                job.collaborators, job.is_finished]
        works.append(work)
    return render_template('jobs.html', jobs=works)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.Password.data != form.Valid_password.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.Login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.Name.data,
            email=form.Login.data,
            surname=form.Surname.data,
            age=form.Age.data,
            position=form.Position.data,
            speciality=form.Speciality.data,
            address=form.Address.data,

        )
        user.set_password(form.Password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        user.check_password(form.password.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = CreateJob()
    db_sess = db_session.create_session()
    if form.validate_on_submit():
        if db_sess.query(Jobs).filter(form.job.data == Jobs.job).first():
            job = db_sess.query(Jobs).filter(form.job.data == Jobs.job).first()
            if job.team_leader == form.team_leader.data or form.team_leader.data == 1:
                job.job = form.job.data
                job.work_size = form.work_size.data
                job.collaborators = form.collaborators.data
                job.is_finished = form.is_finished.data
                db_sess.commit()
                return redirect('/')
            else:
                return render_template('create_job.html', title='Добавление работы', form=form,
                                       message='У пользователя нет доступа')
        else:
            job = Jobs(
                team_leader=form.team_leader.data,
                job=form.job.data,
                work_size=form.work_size.data,
                collaborators=form.collaborators.data,
                is_finished=form.is_finished.data

            )
            db_sess.add(job)
            db_sess.commit()
            return redirect('/')
    return render_template('create_job.html', title='Добавление работы', form=form)


@app.route('/deletejob', methods=['GET', 'POST'])
def delete_job():
    form = DeleteJob()
    db_sess = db_session.create_session()
    if form.validate_on_submit():
        if db_sess.query(Jobs).filter(form.job.data == Jobs.job).first():
            job = db_sess.query(Jobs).filter(form.job.data == Jobs.job).first()
            if job.team_leader == form.team_leader.data or form.team_leader.data == 1:
                db_sess.delete(job)
                db_sess.commit()
                return redirect('/')
            else:
                return render_template('create_job.html', title='Добавление работы', form=form,
                                       message='У пользователя нет доступа')
        return render_template('delete_job.html', title='Удаление работы', form=form, message='Работа не найдена')
    return render_template('delete_job.html', title='Удаление работы', form=form)


if __name__ == '__main__':
    db_session.global_init('db/mars_explorer.db')
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000, host='127.0.0.1')

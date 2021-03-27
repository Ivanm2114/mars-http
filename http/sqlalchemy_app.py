from wtforms.fields.html5 import EmailField

from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager, login_user
from flask import Flask, request, render_template, make_response
from flask import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    Login = StringField('Login / Email', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Valid_password = PasswordField('Repeat password', validators=[DataRequired()])
    Surname = StringField('Surname', validators=[DataRequired()])
    Name = StringField('Name', validators=[DataRequired()])
    Age = IntegerField('Age', validators=[DataRequired()])
    Position = StringField('Position', validators=[DataRequired()])
    Speciality = StringField('Speciality', validators=[DataRequired()])
    Address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
def f():
    db_sess = db_session.create_session()
    works = []
    for job in db_sess.query(Jobs).all():
        work = [job.job, job.leader.surname + ' ' + job.leader.name, str(job.work_size) + ' hours',
                job.collaborators, job.is_finished]
        works.append(work)
    return render_template('jobs.html', jobs=works)


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register_form.html', form=form, title="Registration")


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


if __name__ == '__main__':
    db_session.global_init('db/mars_explorer.db')
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000, host='127.0.0.1')

import datetime

from flask import Flask, request, render_template, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data import db_session, jobs_api
from data.jobs import Jobs
from data.users import User
from data.category import Category
from data.departments import Department
from forms.user import RegisterForm, LoginForm
from forms.jobs import CreateJob, EditJob
from forms.departments import CreateDepartment, EditDepartment

db_session.global_init('db/mars_explorer.db')
db_sess = db_session.create_session()

cat = db_sess.query(Category).filter(Category.id == 3).first()
job = db_sess.query(Jobs).filter(Jobs.id == 3).first()
job.categories.remove(cat)
cat = db_sess.query(Category).filter(Category.id == 4).first()
job.categories.append(cat)

db_sess.commit()

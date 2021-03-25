from flask import Flask, request, render_template
from flask import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register_form.html', form=form, title="Registration")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000, host='127.0.0.1')


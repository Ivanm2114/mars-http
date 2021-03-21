from flask import Flask, request, render_template
from flask import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from data import db_session

import json
from random import choice

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
photos = ['paysage1.png', 'paysage2.png', 'paysage3.png']

class LoginForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/')
def f():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    arr = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(arr)


@app.route('/image_mars')
def show_image():
    return '''
    <head>
        <title>Привет, Марс!</title>
        <h1>Жди нас, Марс!</h1>
        <img src=static/data/mars_planet.png>
        
    </head>
    
    '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
       <head>
           <meta charset="utf-8">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
           <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
           <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" />
           <title>Колонизация</title>
           <h1>Жди нас, Марс!</h1>
           <img src=static/data/mars_planet.png>
       </head>
       <body>
          <div class="alert alert-primary" role="alert" >
                      Человечество вырастает из детства
                    </div>
         <div class="alert alert-secondary" role="alert" >
                      Илон Маск сосаааааааааат
                    </div>
        <div class="alert alert-warning" role="alert" >
                      Роскосмос лууууууучшееееееее
                    </div>
        <div class="alert alert-danger" role="alert" >
                     Займы без документов 88005555335
                    </div>

       </body>
       '''


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img class="d-block w-100" data-src="..." alt="First slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="..." alt="Second slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="..." alt="Third slide">
                        </div>
                      </div>
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        with open('data.txt', encoding='utf-8', mode='w') as file:
            file.write('\n'.join([request.form['surname'],
                                  request.form['name'],
                                  request.form['education']]) + '\n')
            if 'Пилот' in request.form:
                if request.form['Пилот'] == 'on':
                    file.write('Пилот' + ' ')
            if 'Инженер-исследователь' in request.form:
                if request.form['Инженер-исследователь'] == 'on':
                    file.write('Инженер-исследователь' + ' ')
            if "Cпециалист по радиационной защите" in request.form:
                if request.form['Cпециалист по радиационной защите'] == 'on':
                    file.write('Cпециалист по радиационной защите' + ' ')
            if "Что-то другое" in request.form:
                if request.form['Что-то другое'] == 'on':
                    file.write('Что-то другое')
            file.write('\n')
            file.write('\n'.join([request.form['sex'],
                                  request.form['about']]) + '\n')
            if "Volonteer" in request.form:
                file.write('True')
            else:
                file.write('False')
        return redirect('/answer')



@app.route('/answer')
def answer():
    data = []
    with open('data.txt', encoding='utf-8', mode='r') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            data.append(line)
    return render_template('answer_form.html', data=data)


@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    return f'''
       <head>
           <meta charset="utf-8">
             <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       </head>
       <body>
       <h1>Мое предложение:{planet_name}</h1>
          <div class="alert alert-primary" role="alert" >
                      Эта планета рядом с Землей
                    </div>
         <div class="alert alert-secondary" role="alert" >
                      На ней много ресурсов
                    </div>
        <div class="alert alert-warning" role="alert" >
                      На ней есть магнитное поле
                    </div>
        <div class="alert alert-danger" role="alert" >
                     Ну она красивая тоже, даааа
                    </div>

       </body>
       '''


@app.route('/result/<nickname>/<int:level>/<float:rating>')
def show_result(nickname, level, rating):
    return f'''
       <head>
            <title>Результаты</title>
           <meta charset="utf-8">
             <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       </head>
       <body>
       <h1>Результаты отбора</h1>
       <h2>Претендента {nickname}</h2>
          <div class="alert alert-primary" role="alert" >
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
         <div class="alert alert-secondary" role="alert" >
                      составляет {rating}
                    </div>
        <div class="alert alert-warning" role="alert" >
                      Желаем удачи!
                    </div>
       </body>
       '''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                                <div class="alert alert-primary" role="alert" >
                                    <form method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="photo" name="file"> 
                                        </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button> 
                                    </form>
                                </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file'].filename
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <div class="alert alert-primary" role="alert">
                             <img src=static/data/{f}>
                            </div>
                          </body>
                        </html>'''


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                    
                                </div>
                               <button type="submit" class="btn btn-primary">Отправить</button> 
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file'].filename
        print(f)
        return f'''
        <head>
            <title>Привет, Марс!</title>
            <h1>Жди нас, Марс!</h1>
            <img src=static/data/{f}>

        </head>

        '''


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    global photos
    if request.method == 'GET':
        return render_template('carousel.html', photos=photos, title="Пейзажи Марса")
    elif request.method == 'POST':
        photos.append(request.files['file'].filename)
        return redirect('/carousel')



@app.route('/index/<title>')
def preparement(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training_image(profession):
    return render_template('training_scheme.html', profession=profession.lower())


@app.route('/list_prof/<mode>')
def profs_list(mode):
    profs = ['Пилот', 'Криптобиолог', 'Грузчик', 'Врач']
    return render_template('list_prof.html', profs=profs, mode=mode)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('auth.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/distribution')
def distribution():
    return render_template('distribution.html')

@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=int(age), title="Каюты")


@app.route('/members')
def members():
    with open("templates/members.json", encoding='utf-8') as file:
        data = json.load(file)
        member = data['members'][choice(list(data['members'].keys()))]
        member['professions'] = ' '.join(sorted(member['professions']))
    return render_template('member.html', member=member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

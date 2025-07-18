# Введение во Flask
# MVC - Model View Controller
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет все на сервере из контекста запроса
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных
# JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping
# DBeaver - универсальная программа для работы с базой данных

# https://github.com/ipapMaster/Python_Web_2025/blob/Lesson17/templates/login.html
# $ndsp; - добавить строку в html

# pip install flask-wtf
# pip freeze > requirements.txt

import os.path
import sqlite3


from openpyxl.styles.builtins import title
from werkzeug.utils import secure_filename
from flask import Flask, url_for, request, render_template, redirect
from forms.loginform import LoginForm
from forms.user import Register
from data import db_session
from  data.users import User
from data.news import News

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSION = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html', **params)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = Register()
    if form.validate_on_submit():
        # Если пароли не совпали
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', message='Пароли не совпадают', form=form)
        db_ses = db_session.create_session()
        # Если пользователь с таким Е-mail уже есть в базе
        if db_ses.query(User).filter(User.email == form.email.data).first():
            return  render_template('register.html', title='Регистрация', message='Такой пользователь уже есть', form=form)
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_ses.add(user)
        db_ses.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title='Не найдено')



# return Возвращает только строковое представление

@app.route('/news')
def news():
    db_ses = db_session.create_session()
    all_news = db_ses.query(News).filter(News.is_private != True).all()
    # print(all_news)
    return render_template('news.html', title='Новости', news=all_news)


@app.route('/about')
def about():
    # print('Вызвана ф-ция about')
    return render_template('about.html', title='О нас')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Свяжитесь с нами')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    # return f'<img src="./static/images/kaa.jpg">'
    # return f'<img src="{url_for('static', filename='images/kaa.jpg')}">'
    return f'<img src="{url_for('static', filename='images/kaa.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Картинка питона</title>
</head>
<body>
    <img src="{url_for('static', filename='images/kaa.jpg')}" alt="Python">
</body>
</html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('Temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# <string> - по умолчанию
# <int:number> - целое число
# <float:number> - вещественные числа
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в НЕХ-формате)
@app.route('/greeting/<user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


# f'
@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Где номер записи?'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    name, city = result
    cur.close()
    con.close()
    return f'''<table border="2">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>   
    </table>'''


@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['gender'])
        print(request.form['email'])
        print(request.form['about'])
        print(request.form['level'])
        print(request.form)
        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return 'Ошибка загрузки!'


# @app.route('/numbers/')
# @app.route('/numbers/<int:number>')
# def odd_even(number):
#     if number is None:
#         return render_template('numbers.html', title='Где число?', number='')
#     return render_template('numbers.html', title='Чёт-нечёт', number=number)


@app.route('/deals')
def printlist():
    deal = ['помыть', 'выгулять', 'снять', 'сходить']
    return render_template('printlist.html', deals=deal)


@app.route('/queue')
def queue():
    # loop.index - номер итерации, начиная с 1
    # loop.index0 - номер итерации, начиная с 0
    # loop.ferst - True, если первая итерация
    # loop.last - True, если последняя итерация
    return render_template('vars.html', title='Стоим в очереди')


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='localhost', port=5000, debug=debug)
    # ----------='127.0.0.1'
    # user = User()
    # db_sess = db_session.create_session()
    # first = db_sess.query(User).filter((User.id != 1) | (User.email.not_like('%a%'))).all()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # user.name = 'Billy'
    # user.set_username('Bouns')
    # news = News(title='First News', content='News Content', user_id=user.id, is_private=False)
    # db_sess.add(news)
    # db_sess.delete(user)
    # print(user)


    # db_sess.commit()

    # user.name = 'Анатолик'
    # user.name = 'WWWW'
    # user.about = 'Данные по User2'
    # user.email = 'a1@b.ru'
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
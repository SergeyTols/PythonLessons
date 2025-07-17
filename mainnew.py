# Введение во Flask
# MVC - Model View Controller
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет все на сервере из контекста запроса
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных
# JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping

# https://github.com/ipapMaster/Python_Web_2025/blob/Lesson17/templates/login.html

# pip install flask-wtf
# pip freeze > requirements.txt

import os.path
import sqlite3

from openpyxl.styles.builtins import title
from werkzeug.utils import secure_filename
from flask import Flask, url_for, request, render_template
from forms.loginform import LoginForm

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


# return Возвращает только строковое представление

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
    app.run(host='localhost', port=5000, debug=debug)
    # ----------='127.0.0.1'

# Введение во Flask
# MVC - Model View Controller
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет все на сервере из контекста запроса
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных

import sqlite3
from fileinput import filename
from flask import Flask, url_for, request

app = Flask(__name__)
debug = False


@app.route('/')
@app.route('/index')
def index():
    return 'Привет, Flask'  # Callback функция


# return Возвращает только строковое представление

@app.route('/about')
def about():
    print('Вызвана ф-ция about')
    return 'О нас'


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


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)
    # ----------='127.0.0.1'

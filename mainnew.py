# Введение во Flask
# MVC - Model View Controller
from fileinput import filename

from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)
    # ----------='127.0.0.1'

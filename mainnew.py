# Введение во Flask
# MVC - Model View Controller
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)
    # ----------='127.0.0.1'

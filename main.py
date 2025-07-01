## Функции
# Scope (local or global) - область видимости переменной
# Синтаксис:
# def <имя функции>([параметры]):
#     команды
# Если функция ничего не возвращает - это процедура
# В функцию передается копия глобальной переменной
from itertools import count

person = 'Пётр'  # (global) глобальная переменная
count = 0

def greet():
    print('Привет')


greet()
greet()


def greet_to_name(name='noneme'):  # функция задана с ПАРАМЕТРОМ   #| (local) локальная переменная
    print('Привет', name)                                # |


greet_to_name('Вова')  # функция вызвана с АРГУМЕНТОМ


greet_to_name()


def increment():
    global count     # доступ к глобальной переменной из функции
    count += 1
    print(count)


def print_list(array=None):
    if array is None:
        array = []
    for item in array:
        print(item)


increment()
print_list(['мясо', 'рыба', 'тесто', 'детство'])



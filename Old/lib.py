from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'круг'

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def get_name(self):
        return self.name


class Square:
    def __init__(self, side):
        self.side = side
        self.name = 'квадрат'

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def get_name(self):
        return self.name


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = 'прямоугольник'

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self.name


# Book('Язык С++','Бьярн Страупструп')
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это библиотека, а исполняемый: mainnew.py')


# print(__name__)

class Car:
    counter = 0  # Сеатичное свойство (счетчик машин)

    def __init__(self, brand='Noname', model='Nomodel', color='black'):
        self._brand = brand  # 'Skoda'
        self._model = model  # 'Octavia'
        self._color = color  # 'red'
        self.engine_on = False
        Car.counter += 1

    def set_brand(self, new_brand):
        if new_brand:
            self._brand = new_brand

    def set_model(self, new_model):
        if new_model:
            self._model = new_model

    def set_color(self, new_color):
        if new_color:
            self._color = new_color

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def start_engine(self) -> None:
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self._brand} {self._model}')
        else:
            print('Двигатель не заведен, не едем')

    @staticmethod
    def get_counter():
        return Car.counter


# class Person:
#     def __init__(self, name='Sergey', age=1):
#         # свойства (поля) класса
#         self._name = name
#         self._age = age
#
#     # Setter
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#     def set_age(self, new_age):
#         if 0 < new_age < 150:
#             self._age = new_age
#         else:
#             print('Некоректный возраст — ', new_age)
#
#     # Getters
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def person_info(self):
#         print(f'Человек с именем {self._name}, возраст - {self._age}')
#
#
# class Student:
#     def __init__(self, name='Sergey', univ=''):
#         # свойства (поля) класса
#         self._name = name
#         self._univ = univ
#
#     # Setter
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#     def set_univ(self, new_univ):
#         if new_univ:
#             self._univ = new_univ
#
#     def get_name(self):
#         return self._name
#
#     def get_univercity(self):
#         return self._univ
#
#
# class Employee:
#     def __init__(self, name='Sergey', comp=''):
#         # свойства (поля) класса
#         self._name = name
#         self._company = comp
#
#     # Setter
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#     def set_comp(self, new_company):
#         if new_company:
#             self._company = new_company
#
#
#     # Getters
#     def get_name(self):
#         return self._name
#
#     def get_company(self):
#         return self._company



class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Separator:
    def __init__(self):
        self._odd = []
        self._even = []

    def add_num(self, num):
        if num % 2:
            self._even.append(num)
        else:
            self._odd.append(num)

    def get_even(self):
        return self._even

    def get_odd(self):
        return self._odd


class Sorter:
    def __init__(self):
        self._words = []

    def add_word(self, word):
        self._words.append(word)

    def result(self):
        return sorted(self._words, key=lambda x: len(x), reverse=True)


class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, weight):
        pass

    def add_left(self, weight):
        pass

    def result(self) -> str:
        return  # состояние весов
# Duck type - утиная типизация (прочитать)
#
#
# ООП (polymorphism)
# method override; operator overloading
# полиморфизм - св-во кода работать с разными типами данных
# Функция isinstance() проверяет, является ли объект (первый аргумент)
#            экземпляром или подклассом класса classinfo (второй аргумент
# isinstance() -> True
# isinstance
#
from lib import Circle, Square, Rectangle


# def shape_info(shape):
#     print(f'Площадь {shape.get_name()}а: {shape.area()}\n'
#           f'Периметр {shape.get_name()}а: {shape.perimetr()}\n')

rect, c, sqr = ['прямоугольник', 'круг', 'квадрат']

def shape_info(shape: object):
    if isinstance(shape, Circle):
        fig = c
    if isinstance(shape, Rectangle):
        fig = rect
    if isinstance(shape, Square):
        fig = sqr
    print(f'Площадь {fig}а: {shape.area()}\n'
          f'Периметр {fig}а: {shape.perimetr()}\n')


s = Square(10)
shape_info(s)

cr = Circle(10)
shape_info(cr)

r = Rectangle(10, 5)
shape_info(r)

# from lib import Book
#
# book = Book('Язык С++','Бьярн Страупструп')
#
# print(f'{book.get_title()}, {book.get_author()}')

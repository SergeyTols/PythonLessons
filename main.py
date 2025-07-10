# Duck type - утиная типизация (прочитать)
# Шпоргалка по всем методам в пайтон
#
# ООП (inheritance)
# класс, от которого наследуем: базовый, родительский, суперкласс
# класс, который наследуется: производный, дочерний
from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    def info(self):
        print(f'Класс: {self.__class__.__name__}')

    @abstractmethod
    def aria(self):
        pass  # Или: return None

    @abstractmethod
    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = 'круг'

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def get_name(self):
        return self.name


class Rectangle(Shape):
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


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = 'квадрат'
        # self.side = side

    # def perimetr(self):
    #     return 4 * self.side
    #
    # def area(self):
    #     return self.side ** 2

    # def get_name(self):
    #     return self.name


class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)
        self.name = 'треугольник'
        self.side = side

    def perimetr(self):
        return 3 * self.side

    #
    def area(self):
        return (self.side ** 2 * 3 ** 0.5) / 4


s = Square(5)
print(s.area())
print(s.perimetr())
print(s.get_name())
s.info()

tr = Triangle(8)
print(tr.area())
print(tr.perimetr())
print(tr.get_name())
tr.info()
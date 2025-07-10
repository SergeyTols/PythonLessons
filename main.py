# Duck type - утиная типизация (прочитать)
# Шпоргалка по всем методам в пайтон
#
# ООП (magic methods)
# method override; operator overloading
#
#
#
from math import hypot

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<Point: ({self.x}, {self.y})>'

    def __repr__(self):
        return f'<List of Point: ({self.x}, {self.y})>'

    def __sub__(self, other):
        # return Point(self.x - other.x, self.y - other.y)
        return Point(abs(self.x - other.x), abs(self.y - other.y))

    def __add__(self, other):
        # hypot = (abs(self.x - other.x), abs(self.y - other.y))
        # abs(self.x - other.x), abs(self.y - other.y)
        return hypot((self.x - other.x), (self.y - other.y))


# a = round(hypot(5, 2))
p = Point(5, 4)
po = Point(10, 2)


print(p - po)




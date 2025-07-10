# Duck type - утиная типизация (прочитать)
#
#
# ООП (magic methods)
# method override; operator overloading
#
#
#

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<Point: ({self.x}, {self.y})>'

    def __repr__(self):
        return f'<List of Point: ({self.x}, {self.y})>'

p = Point()
po = [Point(), Point()]
print(p)
print(po)


# Duck type - утиная типизация (прочитать)
# Шпоргалка по всем методам в пайтон
#
# ООП (magic methods)
# method override; operator overloading
# __call__ - экземпляр класса становится вызываем как ф-ция
#
#
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

s = SquareFunction(1, 2, 3)
print(s(2))
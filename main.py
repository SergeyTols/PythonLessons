#  Возвращение нескольких значений из ф-ции
#  при распаковке "*" может быть только у одного аргумента
from tkinter.font import names


def coordinates() -> tuple:
    return 5.4, 3.2, 3.9, 6.5, 4.0


x, y, *rest = coordinates()    # распаковка (кортежа)  # *rest - список oставшихся значений.
print(f'x = {x}, y = {y}, rest = {rest}')

*names, surname = 'Остап Сулейман Бендер'.split()
print(names, surname)
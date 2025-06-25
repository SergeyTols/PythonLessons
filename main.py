# Ctrl + Shift + стрелка вверх/вниз - двигать выделенное
# Ctrl + Shift + стрелка вправо - выделить слово
# Ctrl + z - отмена
# PEP 8     Alt + Ctrl + L
# Ctrl + /  - закоментить строку (на русском "спрятать")

# name = 'Сергей'  # str
# name = input('Как тебя зовут? ')  # str
# surname = 'Петров'
# age = 27  # int
# temper = 13.4  # float (floating point)
#
# print('привет,', name, surname, 'тебе', age, 'лет')
# print('На улице', temper)

# donut = input('Стоимость пончика: ')
# coffee = input('Стоимость кофе: ')
#
# print('С вас', int(coffee) + int(donut), 'руб.')

# donut = int(input('Стоимость пончика: '))
# coffee = float(input('Стоимость кофе: '))
#
# print('С вас', coffee + donut, 'руб.')

number = int(input('Vvedi '))
print('Число', number, 'в степени 3 будет', number ** 3)
print('Квадратный корень от', number, 'будет:', number ** (1 / 2))

temp = """
Вансив
Авансив
"""

print(temp)

'''
== - равно
!= - не равно
indent - кочка, отступ
unindent - возврат отступа

    Правописание if:
if <условие>:
    команды
'''

promt = """Виитязь на распутье
Налево (L) пойдёшь, волю обретешь...
Направо (R) пойдёшь, коня потеряешь...
Прямо (F) пойдёшь, то и сыт..."""
print(promt)
choice = input('Куда идём (L, R или F): ')
if choice == 'L' or choice == 'l':
    print('Вольный ты')
elif choice == 'R' or choice == 'r':
    print('Теперь пешком')
elif choice == 'F' or choice == 'f':
    print('теперь сыт!')
else:
    print('Выбор не ясен...')

# на тест

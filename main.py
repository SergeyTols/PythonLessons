# Формат вывода
# \ - вутри строки: начало управляющей последовательности
# word1 = 'пришел\n\t'
# word2 = 'увидел'
# word3 = 'победил'
# word4 = '27\xB0C'
#
# print(word1, word2, word3, sep=', ', end=' -> ')
# print(word4, end='')
# print('   C:\\Prog Fil\\job')

name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
ves = 92.636
#
# # 1 способ (плэйсхолдеры)
# # %s - string
# # %d - digit (целое число)
# # %f - float
# print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))
#
# # 2 способ
# print('Имя: {}, E-mail: {}, Возраст: {}'.format(name, email, age))
#
# # 3 способ
# print(f'Имя: {name}, E-mail: {email}, Возраст: {age}, Вес: {ves:.3f}')

print(f' Имя: {name}\n E-mail:  {email}\n Возраст: {age}\n Вес:     {ves:.3f}')

print(f' Имя: {name:12} E-mail:  {email} Возраст: {age} Вес:     {ves:.3f}')
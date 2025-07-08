# Регулярные выражение (поиск по паттерну)
# alice.yandex.ru
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (без пробелов)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности(32767) {0,}
# + - от одного до бесконечности(32767) {1,}
import re

# pattern = r'\b\w{4}\b' # все слова из 4 символов
# pattern = r'\d' # все цифры от 0 до 9
# pattern = r'\d{3}' # три цифры подряд
# pattern = r'начало!\Z' # на что заканчивается
# pattern = '[0-5][0-9]' # две, идущие подряд
# pattern = '[а-яА-я]' # все буквы от "а" до "я" и от "А" до "Я"
# pattern = '[^ерм]' # исключить символы
# pattern = r'\((.+?)\)' # вытащить текст из скобок
# pattern = 'o{2,5}'
pattern = 'Go{3,}gle'

# test_string = '10 плюс 20, будет 300'
# test_string = 'Главное - начало!'
# test_string = 'Время - 07:55'
# test_string = 'Поиск по образцу (pattern)'
test_string = 'Google, Gooogle, Goooooooogle'


# result = re.search(pattern, test_string)
result1 = re.findall(pattern, test_string)
# print(result)
print(result1)

# print('Цифры есть') if result else print('Цифр нет') # Ternary if (тернарный условный оператор)
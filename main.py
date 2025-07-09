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
# https://regex101.com

import re

pattern = r'[,.:;!]'
test_string = 'яблоко,  груша.   банан   ;  слива !    абрикос  '
# test_string = ''.join(test_string.split()) # убрали все пробелы

result1 = re.split(pattern, test_string)
# через map
# result1 = list(map(lambda x: x.strip(), result1))

# через list comprehension с сортировкой
result1 = sorted(x.strip() for x in result1)
print(result1)


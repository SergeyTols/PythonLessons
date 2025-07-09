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
import requests

pattern = r'<img[^>]+src="([^">]+)"'

# test_string = '<img height="50" width="150" src="images/bg.jpg">' # Сначала проверим

html = requests.get('https://skillbox.ru').text
result1 = re.findall(pattern, html)

print(result1)


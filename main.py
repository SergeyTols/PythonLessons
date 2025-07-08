# Регулярные выражение (поиск по паттерну)
# alice.yandex.ru
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)

import re

pattern = r'\b\w{4}\b'
test_string = '10 плюс 20, будет 30'

result = re.search(pattern, test_string)
result1 = re.findall(pattern, test_string)
print(result)
print(result1)

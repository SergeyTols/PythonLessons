# startswith (начало строки) и endswith (конец строки)

# 1. find('подстрока')  поиск с начала строки
# 2. find('подстрока', start) с позиции start
# 3. find('подстрока', start, end) c ... по ...



s = 'тиливизор'

print(s.replace('и','е', 2))



s = '+7-012-345-67-89'  # => +7 (012) 345-67-89

res = s.replace('-', ' (', 1)
res = res.replace('-', ') ', 1)

print(res)
print(s.replace('-', ' (', 1).replace('-', ') ', 1))


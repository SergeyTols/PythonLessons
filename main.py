# Встроеннные библиотеки
# PyPI - Python Package Index (pypi.org)
# sample (в отличие от choice) выбирает уникальные (без повторов)
# s
import random as r
# r.seed()
# print(r.random())

abc = 'wqertyuiopasdfghjklzxcvbnm'
# lst = list(abc) + ['1', '2'] + ['#', '$']
N = 8
num = '1234567890'
spec = '!@#$%'

abc = list(abc)
num = list(num)
spec = list(spec)

temp = abc[:N - 3]
temp.append(r.choice(abc).upper())
temp.append(r.choice(num))
temp.append(r.choice(spec))
r.shuffle(temp)
res = ''.join(temp)

print(res)

# zara = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
#
# for _ in range(10):
#     print(r.choice(zara), r.choice(zara))
#
# d = {'a': 1,
#      'b': 2,
#      'c': 3,
# }
# keys = list(d.keys())
#
# key = r.choice(keys)
# print(d[key])

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for _ in range(5):
#     print(r.sample(lst, k=5))

# print(r.choice(['орёл', 'решка']))
# print(r.choice('орёл'))

# print(r.choice(lst))

# for _ in range(10):
#     r.randint(0, 10)
#     print(r.randrange(0, 10, 2))

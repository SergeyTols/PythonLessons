## Списочные выражения (list comprehension)

squares = []
for i in range(10):
    squares.append(i ** 2)
print(*squares, sep=', ')

#   Список квадратов чисел
squares = [i ** 2 for i in range(10)]
print(*squares, sep=', ')

#   Список квадратов четных чисел

#         | что | |     закон      | |   условие  |
squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(*squares, sep=', ')

#   произведение i и j
# for i in range(3):
#     for j in range(3):
#        print(i * j)
print([i * j for i in range(3) for j in range(3)], sep=', ')
print(*[i * j for i in range(3) for j in range(3)], sep=', ')

#   Строку чисел в список
n = '500 600 700 800'
approved = [500, 800]
print([int(i) for i in n.split()])

#   какие-то действия со списком "а"
a = [int(i) for i in n.split()]
print(a)
print([int(i) for i in n.split() if int(i) in approved])




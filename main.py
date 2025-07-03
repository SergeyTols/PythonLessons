# Рекурсия - функция вызывает сама себя

# def factorial(count): # 5! = 1 * 2 * 3 * 4 * 5
#     result = 1
#     for i in range(2, count +1):
#         result *= i
#     return result
# for x in range(10):
#     print(x, factorial(x))

def factorial(x: int):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x - 1)


for x in range(11):
    print(x, factorial(x))

# Потоковый ввод sys.stdin (Ctrl + D)
# import sys
# from idlelib.tooltip import OnHoverTooltipBase
# from operator import index
#
# # data = sys.stdin.readlines()
# #
# # data = [d.strip('\n') for d in data]
#
# data = [d.strip('\n') for d in sys.stdin.readlines()]
# temp = []  # индекс строки в data и число слов в виде кортежей
# for i, s in enumerate(data):
#     temp.append((i, len(s.split())))
# temp.sort(key=lambda x: x[1])
# index = temp[0][0]
# res = sorted(data[index].split())
# print(*res, sep='-')

# раз два три
# елочка гори

# for line in sys.stdin:
#     print(line)

# any - любой элемент коллекции вернул True
# all - все эл-ты коллекции вернули True

# print(all([1, 2, 3])) # все эл-ты ненулевые
# print(all([1, 2, 0])) # один элемент нулевой
# print(all([]))
#
# words = 'один два три'.split()
#
# # list_for_analize = list(map(lambda x: len(x) > 2, words))
# print(any(list(map(lambda x: len(x) > 5, words))))

# fruits = ['ананас', 'банан', 'ежевика', 'арбуз', 'малина']
#
# # print(sorted(fruits, key=lambda s: (len(s), s[-1])))
#
# goods = [
#     ['Утюг', 1000, 2],
#     ['Фен', 1000, 5],
#     ['Телевизор', 8000, 3],
# ]
#
# print(sorted(goods, key=lambda s: (s[1], s[2], s[0])))  # Сортировка по цене, кол-ву, имени

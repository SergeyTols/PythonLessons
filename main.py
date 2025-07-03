# Анонимные ф-ции
# Проверка коллекции

# any - любой элемент коллекции вернул True
# all - все эл-ты коллекции вернули True

print(all([1, 2, 3])) # все эл-ты ненулевые
print(all([1, 2, 0])) # один элемент нулевой
print(all([]))

words = 'один два три'.split()

# list_for_analize = list(map(lambda x: len(x) > 2, words))
print(any(list(map(lambda x: len(x) > 5, words))))

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


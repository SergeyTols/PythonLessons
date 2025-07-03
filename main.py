#   Функция, как объект
#   Функция критерия отбора элементов списка
#   Критерий: длинна слова
def is_longer_six(word):
    # if len(word) > 6:
    #     return word
    return len(word) > 6


def first_c(word):
    return word[0] == 'с'


words = ['В', 'этом', 'списке', 'останутся', 'слова', 'длинна', 'которых',
         'больше', 'шести']

# result = list(filter(is_longer_six, words))
# print(result)
#
# for word1 in filter(is_longer_six, words):
#     print(word1)
#
# result2 = list(filter(first_c, words))
# print(result2)

# res = list(filter(lambda s: 'ан' in s, words))
# print(res)

#  sq = list(map(lambda x : x ** 2, range(3, 16)))
sq = [x ** 2 for x in range(3, 16)]
print(sq)

long_words = [word for word in words if len(word) > 6]
print(long_words)



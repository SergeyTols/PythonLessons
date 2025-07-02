#   Функция, как объект
#   передается в другие функции(функции высшего порядка)
печатник = print
печатник('Привет мир')

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

result = list(filter(is_longer_six, words))
print(result)

for word1 in filter(is_longer_six, words):
    print(word1)

result2 = list(filter(first_c, words))
print(result2)
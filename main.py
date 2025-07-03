#   Функция, как объект
#   Функция критерия отбора элементов списка
#   Критерий: длинна слова
from os import remove


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

ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
       set([x.upper() for x in ENGLISH_ABC]) ^
       set([x.upper() for x in RUSSIAN_ABC]))
print(ABC)
# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)
txt ='Однажды, теперь, завтра!'

def remove_punctuation(text):
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))

def get_words(text: str) -> list:
    return remove_punctuation(text).split()

def long_words(text, length=4) -> filter:
    return filter(lambda word: len(word) >= length, get_words(txt))

print(list(long_words(txt)))
print(remove_punctuation(txt))

# text = ''.join(filter(lambda x: x in ABC ^ {' '}, txt))
# print(text)

# numbers = [1, 2, 3, 4, 5]   # list(range(1, 6))
# squares = {n: n ** 2 for n in numbers}
# print(squares)

numbers = range(1,11)
squar = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(squar)

source_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}
dest_dict = {k: v * 2 for k, v in source_dict.items()}
print(dest_dict)
# phrase = 'ЯзыК PythoN'
#
# print(phrase.upper()) # все маленькие
# print(phrase.lower()) # все большие
# print(phrase.capitalize()) # только первая большая
# print(phrase.title()) # все с большой
# print('Ура!' * 3)
# print('телевизор'.count('е'))
# print('Python'.index('h')) # узнать индекс первой подходящей буквы в слове


# for ch in (word := input('Введите слово: ')):
#     i = word.index(ch)
#     print(ch * (i + 1), end='')

# word = 'привет'
# for i in range(len(word) + 1):
#     print(word[i - 1] * i, end='')

word = '          статор            '

print(word.strip()) # убрать пробелы справа и слева
print(word.lstrip()) # убрать пробелы слева
print(word.rstrip())# убрать пробелы справа

word = 'ротор'

print(word.strip('р')) # убрать символ справа и слева
# Циклы:
# word = ''
# while len(word := input('Введите слово длинее 3 символов: ')) <= 3:
#     word = input('Введите слово длинее 3 символов: ')
#     print(f'{word} хорошее слово')
#
# print(f'ghfdbkmyj: "{word}"')

# Цикл до ввода пустой строки
# без :=
word = input('Введите слово: ')
while word != '':
    print(f'Слово: {word}')
    word = input('Введите слово: ')

print('Пустая строка')

# c использованием :=
while (word := input('Введите слово: ')) != '':
    print(f'Слово: "{word}"')
print('Пустая строка')
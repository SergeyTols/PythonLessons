# Строки (immutable, iterable) - неизменяемый тип данных
#    012345
s = 'Python'
# s[3] = 'y' error (immutable)
# Индекс может быть отрицательным (с конца)
print(s[0])


words = 'язык питон'
vovel = 0

for ch in words: #
    if ch in {'а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы'}:
        vovel += 1
    # if ch in 'аеиоуэюяы':
    #     vovel += 1
print(f'гласных в строке "{words}" = {vovel}')

# перебор строки по числовому индексу
for index in range(len(words)):
    print(words[index], end=' ')
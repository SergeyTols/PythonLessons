#  Списки
#  Создание аббревиатур

lst = []
res_lst = ''
while (word := input('Введите слово: ').strip()) != '':
    lst.append(word[0].upper())

print('Получилось', end=': ')
print(*lst[:10], sep='')
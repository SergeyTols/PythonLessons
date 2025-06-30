# a = ['a', 'b', 'c']
# # b = a
# b = a[:]  #  b = a.copy()  - синонимы
# b.append('d')  # b += ['d']
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# lst = []
# while (item := input('Ведите ингредиенты: ')) != '':
#     lst.append(item)
# print(f'У нас есть {len(lst)} ингредиентов')
# lst.sort()
# for i in range(len(lst)):
#     print(f'\t{i + 1}. {lst[i]}')

lst = []
while (item := input('Ведите ингредиенты: ')) != '':
    lst.append(item)  #добавить в список

temp = set(lst)    # Убрать
lst = list(temp)   #  повторения

print(f'У нас есть {len(lst)} ингредиентов')

lst.sort()   # сортировка списка
for i in range(len(lst)):
    print(f'\t{i + 1}. {lst[i]}')  # вывод списка


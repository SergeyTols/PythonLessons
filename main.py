# Коллекции (set, list, dict, tuple)
# Множества
s = set() # пустое множество
# print(dir(s)) - список метедов множества
s = {'3', '5', '7', '3', '3'}
s.add(8)
s.add('8') # добавить
s.remove('3') # удалить, вызывает ошибку, если нет
s.discard('8') # удалить, удаляет вслепую
# s.clear() # очищает множество
temp = s.pop() # удаляуе случайный и возвращает его

# Методы: 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
#  'symmetric_difference_update', 'union', 'update']
print(type(s)) # имя класса, тип переменной
print(f'Число эл-тов в "s" = {len(s)}')
print('Есть ли "3"?')
if '3' in s:
    print('да')
else:
    print('нет')
for item in s:
    print(item)
print(s)

for item in s:
    if item == '7':
        print(item)
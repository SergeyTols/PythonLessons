## Словари
# Пустой словарь
# 1. d = {}
# 2. d = dict()

# Предзаполненный словарь
d = {
    'table': ['таблица', 'стол'],
    'well': ['хорошо','колодец','скважина'],
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один',
}
# d['apple'].append('тыблоко')

# print(d['table'])
# print(d[1])
# print(d['well'])
# print(d['well'][1])
# d['plum'] = ['слива']
# d['well'].append('дыра')
# print(d['well'])
# print(d['plum'])
# print(d)

# del d['well']   # Удалить весь список из словаря
# # print(d)    # - словарь целиком, как есть
#
# # Перебор по умолчанию + вывести красивее
# for key in d:
#     print(key, '->', d[key])

deleted_item = d.pop('apple')
print('Удалится элемент: ', deleted_item)

print('Есть ли стул в словаре: ')
if 'chair' in d:
    print('Есть!')
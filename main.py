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
    (55.75, 37.5): 'Москва'
}

print(d[(55.75, 37.5)])

# Перебор по умолчанию + вывести красивее
# for key in d:
#     print(key, '->', d[key])

# for key in d.keys(): # Перебор ключей
#     print(key, '->', d[key])
#
# for values in d.keys(): # Перебор значений
#     print(values, '->', d[values])
#
# for k, v in d.items():
#     print(k, '->', v)

# print(d.keys())
# print(d.values())

# deleted_item = d.pop('apple')
# print('Удалится элемент: ', deleted_item)
#
print('Есть ли стул в словаре: ')
if 'chair' in d:
    print('Есть!')

print('Доступ к несуществующему ключу без "исключений"')
pear = d.get('pear', 'Груши нет')  # .get() - мягкое обращение к ключу
print('Где груша: ', pear)
#       Позиционные | Именованные
def print_any(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(k, '=', v)


print_any('Дмитрий', 'Колесов', city='Москва', age=27)


def profile(name, surname, city, *children, **additional):
    print(f'Имя: {name}')
    print(f'Фамилия: {surname}')
    print(f'Из города: {city}')
    if len(children) > 0:
        print('Дети:',', '.join(children))
    if 'hobbie' in additional:
        print('Хобби:', ', '.join(additional['hobbie']))
    # print(additional)


profile('Дмитрий', 'Колесов', 'Волгоград', 'Мария', 'Петр', hobbie=['Филателия', 'Шахматы'])
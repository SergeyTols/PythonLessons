# Исключения (runtime)
# try:
#   <что пытаемся сделать>
# except:
#   <брабатываем исключения>
# else:
#   <если исключений не было>
# finally:
#   <выполняется в любом случае>

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

loop = True
while loop:
    try:
        index = int(input('Введите индекс: '))
        if not index < len(lst):
            raise ValueError('Введенный индекс вне диапазона')
        print(f'Число по индексу {index}: {lst[index]}')
    except ValueError as exp:
        print('Надо быть внимательнее:', exp)
    else:
        loop = False
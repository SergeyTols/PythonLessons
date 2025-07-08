# Исключения (runtime)
# try:
#   <что пытаемся сделать>
# except:
#   <обрабатываем исключения>
# else:
#   <если исключений не было>
# finally:
#   <выполняется в любом случае>

while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print('ужно вводить числа...')
        print(f'А введено {a} и {b} :(')
    else:
        print(result)
        break

# if a.isdigit() and b.isdigit():
#     else:
#         print(int(a) / int(b))


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# loop = True
# while loop:
#     try:
#         index = int(input('Введите индекс: '))
#         if not index < len(lst):
#             raise ValueError('Введенный индекс вне диапазона')
#         print(f'Число по индексу {index}: {lst[index]}')
#     except ValueError as exp:
#         print('Надо быть внимательнее:', exp)
#     else:
#         loop = False
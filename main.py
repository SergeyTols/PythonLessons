# Исключения (runtime)
# try:
#   <что пытаемся сделать>
#except:
#   <брабатываем исключения>
#else:
#   <если исключений не было>
# finally:
#   <выполняется в любом случае>

print('Остаток от деления: ')
loop = True
while loop:
    try:
        value = int(input('На что делим число 10:'))
        res = 10 % value
        print(f'Остаток от деления 10 на {value} = {res}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print('Надо вводить только целые числа')
    except Exception as exp:
        print('Произошло исключение: ', exp.__class__.__name__, exp)
    else:
        loop = False

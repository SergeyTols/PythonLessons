a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
if a == 0:
    print('введи другое "a"')
else:
    b = int(input('b = '))
    c = int(input('c = '))
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('нет корней')
    elif d == 0:
        print(f'корень: {x:.2f}')
    else:
        x1 = (-b + d  ** 0.5) / 2 * a
        x2 = (-b - d  ** 0.5) / 2 * a
        print(f'корни:\n\tx1 = {x1:.2f}\n\tx2 = {x2:.2f}')
# else:
#     print('введи другое "a"')




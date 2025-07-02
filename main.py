#  Функция с переменным числом аргументов

def multy(*args):
    print(len(args))  # подсчет числа аргументов
    print(args)  # вывод по индексу или перебором в цикле
    # if len(args) == 0:
    #     return 0
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result


# multy(1, 2)
print(multy(5.4, 3.2, 4.7))

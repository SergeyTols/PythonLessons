#  Функция с переменным числом аргументов

def multy(*args, first=0):
    # print(len(args))  # подсчет числа аргументов
    # print(args)  # вывод по индексу или перебором в цикле
    # if len(args) == 0:
    #     return 0
    if not args:
        return first
    result = first
    for arg in args:
        result *= arg
    return result


# multy(1, 2)
print(multy(2, 3, 4, first=5))


def fio(name, surname):
    return f'{name} {surname}'


print(fio(name='Остап', surname='Бендер'))




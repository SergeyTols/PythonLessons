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


def calc(*args: tuple, operator: str ='+') -> any:
    match operator:
        case '+':
            result = 0
            for arg in args:
                result += arg
        case '*':
            result = 1
            for arg in args:
                result *= arg
        case _:
            return -float('inf')
    return result
print(calc(2, 3, 4, operator='*'))


def sandwich(type_of_meal, with_onion=False, with_tomato=False):
    print('Булочка')
    if with_onion:
        print('Лук')
    print(type_of_meal)
    if with_tomato:
        print('Помидоры')
    print('Булочка')


sandwich('Котлета', with_onion=True, with_tomato=True)


# Функции
# Return Value
# Чистая ф-ция - ф-ция, не имеющая эффекта на переменные и элементы, не влияет на ход выполнения программы
# Вычисление квадрата числа

def square(num):
    return num ** 2
    # temp = num ** 2
    # return temp



def even_odd(num):
    if num % 2 == 0:
        return 'Четное'
    return 'Нечетное'
    # if num % 2 == 0:
    #     return 'Четное'
    # else:
    #     return 'Нечетное'



print(even_odd(5))
t = square(5)
print(t)

# ДЗ: Функция: Вывести число словами 56 -> триста пятьдесят шесть.
# def num_to_word(num):
#     if str(num) > 2:
#         return
#     e = num % 10
#     le = ['один', 'два']
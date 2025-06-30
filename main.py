# #  Кортеж (tuple, immutable) - тот же список, но не изменяемый; меньше жор памяти, быстрее обработка
# #  можно спросить длинну, перебрать содержимое в цикле
# BLACK = (0, 0, 0)
# empty = ()  #  tuple()
# ane = (1,)  #  так пишется кортеж из 1 эл-та
# temper = 36,6  #  кортеж из 2-х эл-тов
# s = 'python'
# t = tuple(s) + ('.',)
# print(t)
# print(7 > 3)
# cards = [(7, 'червей'), ('туз','пик')]
# print((1, 2) > (1, 3))


# channels = ['red', 'green', 'blue']
# channels2 = 'ABC'
# channels3 = {1, 2, 3}
#
# # r, g, b = channels  #  распаковка
# # r, *g = channels3  #  частичная расспаковка
# r, *channels3 = channels3
# print(channels3)

a, b, c = input('= '), input('= '), input('= ')
a, b, c = [1, 2], 3, 4  #  упаковка (для а)



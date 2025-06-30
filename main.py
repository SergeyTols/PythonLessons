# #  Кортеж (tuple, immutable) - тот же список, но не изменяемый; меньше жор памяти, быстрее обработка
# #  можно спросить длинну, перебрать содержимое в цикле
#  help(sorted)
#   Функция enumerate() - в цикле for возвращает пару (index, v)

fio = ['Вова', 'Вася', 'Петя']

# for item in enumerate(fio):
#     print(item)

for i, v in enumerate(fio):
    print(f'{i + 1}. {v}.')

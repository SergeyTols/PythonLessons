# #  Кортеж (tuple, immutable) - тот же список, но не изменяемый; меньше жор памяти, быстрее обработка
# #  можно спросить длинну, перебрать содержимое в цикле

N = 3
studs = []

for _ in range(N):

    name, score = input('Имя: '), float(input('Ср. балл: '))
    studs.append((name, score))

print(studs)
for st in studs:
    name, score = st
    print('Имя: ', name)
    print('Ср. балл: ', score)

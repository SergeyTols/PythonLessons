# startswith (начало строки) и endswith (конец строки)

# 1. find('подстрока')  поиск с начала строки
# 2. find('подстрока', start) с позиции start
# 3. find('подстрока', start, end) c ... по ...

si = 'смотреть, вертеть, видеть'

index = si.find('еть', 10)  # ищем с начала строки "s"

s = 'синхрофазотрон'
ch = 'о'
i = 0
start = 0

if ch in s:
    count = s.count(ch)
    i = s.find(ch, 0)
    stert = i + 1
    print(f'{ch} в "{s}" {count}')

    print(f'Её позиция: {i}', end=' ')

else:
    print(f'в слове "{s}" нет буквы {ch}')

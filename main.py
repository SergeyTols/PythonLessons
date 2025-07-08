# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write - файл открывается на запись(перезаписывается), если его нет, то создается
# a - append - запись в коннец файла
# r - read - чтение
# print(*args, sep=' ', end='\n', file=None, flush=False)
# Файлы и OS-модуль

# fo = open('info.txt', 'wt', encoding='utf-8')
#
# fo.write('4, 2, 4, 6, 3, 5, 9, 7')
# fo.write('\n5, 1, 8, 2, 6, 8, 1, 2')
#
# fo.close()


res = []

with open('info.txt', encoding='utf-8') as f:
    while temp := f.readline().rstrip('\n'):
        res += temp.split(', ')

res = sorted(int(x) for x in set(res))

print(res)
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write - файл открывается на запись(перезаписывается), если его нет, то создается
# a - append - запись в коннец файла
# r - read - чтение
# print(*args, sep=' ', end='\n', file=None, flush=False)
# Файлы и OS-модуль

import pickle
import pprint

d = {
    'стол': 'table',
    'стул': 'chair',
}

# сериализация
with open('dictfile.dat', 'wb') as p:
    # d - что сериализуем
    # p - куда сериализуем
    pickle.dump(d, p)

# десериализация
with open('dictfile.dat', 'rb') as p:
    d = pickle.load(p)

pprint.pprint(d, width=15)

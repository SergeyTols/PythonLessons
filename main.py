# Файлы - набор данных в виде определенной структуры, сохраненный на носителе с присвоенным именем и, возможно, расширением
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write - файл открывается на запись(перезаписывается), если его нет, то создается
# a - append - запись в коннец файла
# r - read - чтение
# print(*args, sep=' ', end='\n', file=None, flush=False)
# Файлы и OS-модуль

import os

# os.mkdir('libs')

# "Мягкое" создание директории (вместо mkdir)
# os.makedirs('libs', exist_ok=True)

print(os.path.exists('libs')) # проверка существования пути

path = os.getcwd()
os.chdir(path + '/images')

all_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
print(all_files)

all_files = [f for f in os.listdir('.') if f.startswith('K')]
os.chdir('..')
print(all_files)

# if os.path.exists('libs'):
#     os.rmdir('libs') # удаление директории

# path = os.getcwd() # get current working directory
# print(path)
#
# os.chdir(path + '/images')
# print(os.getcwd())
#
# os.chdir('..')
# os.chdir(path + '/fonts')
# print(path)


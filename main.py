# Файлы - набор данных в виде определенной структуры, сохраненный на носителе с присвоенным именем и, возможно, расширением
# name.txt
# t - текстовый файл (txt, html, xml)
# b - бинарные файлы (jpg, avi, mp3)
# w - write - файл открывается на запись(перезаписывается), если его нет, то создается
# a - append - запись в коннец файла
# r - read - чтение
# print(*args, sep=' ', end='\n', file=None, flush=False)

fo = open('info.txt', 'at', encoding='utf-8')

fo.write(' Хороший текст')
# print('А вот это будет уже с новой строки')

fo.close()

# fo = open('info.txt', 'rt', encoding='utf-8')
#
# text = fo.read(11)  # (5) - сколько байт читать
# fo.read(6)  # (5) - сколько байт читать
# # fo.read()  # (5) - сколько байт читать
# text += fo.read(7)
# print('Вот, что было в файле', end=': ')
# print(text)
#
# fo.close()

# fo = open('info.txt', 'wt', encoding='utf-8')
#
# print(fo.mode)
# print(fo.name)
# print(fo.encoding)
#
# count = fo.write('Этот текст будет в файле!')
# print('В файл записано', count, 'байт!')
#
# fo.close()
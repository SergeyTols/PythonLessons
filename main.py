# Исключения (runtime)
# try:
#   <что пытаемся сделать>
#except:
#   <брабатываем исключения>
#else:
#   <если исключений не было>
# finally:
#   <выполняется в любом случае>

flag = False # открывался ли на запись
try:
    fo = open('information.txt', encoding='utf-8')
except FileNotFoundError:
    fo = open('information.txt', 'wt', encoding='utf-8')
    flag = True
    print('Файл не обнаружен и создан с параметрами по умолчанию')
    # with open('information.txt', 'w', encoding='utf-8') as fo:
    #     fo.write('По умолчанию')
else:
    print('Файл открыт успешною Читаем его и закрываем.')
    print(fo.read())
    fo.close()
finally:
    if flag:
        fo.write('По умолчанию')
        fo.close()
    print('Продолжаем работать')

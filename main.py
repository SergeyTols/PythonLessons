# Исключения (runtime)
# try:
#   <что пытаемся сделать>
# except:
#   <обрабатываем исключения>
# else:
#   <если исключений не было>
# finally:
#   <выполняется в любом случае>


#   Практикум (обучаемый словарь)

import pickle


# инимальная версия, если файл dict.dat отсутствует
voc = {
    'стол': 'table',
    'стул': 'chair',
}


# функция для распечатки словаря
def print_voc():
    print('Сейчас словарь содержит: ')
    for k, v in voc.items():
        print(k, '—', v)  # Alt + 0151



# Загружаем словарь из файла
try:
    with open('dict.dat', 'rb') as dump_in:
        voc = pickle.load(dump_in)
except FileNotFoundError:
    with open('dict.dat', 'wb') as dump_out:
        pickle.dump(voc, dump_out)
    print('Создан минимальный словарь: ')
    print_voc()

while True:
    temp = input('\nВведите слово для перевода или "#" для завершения: ')
    word = temp.strip().lower()
    if word == '#' or word == '№':
        break
    if word in voc.keys():
        translate = voc[word]
        print(f'Слово "{word}" переводится как {translate}.\n')
    else:
        print(f'Значение слова {word} тсутствует в словаре.')
        newkey = f'А как слово {word} переводится.\n'
        newkey += 'Если ничего не вводите нажмите ENTER,\n '
        newkey += 'или введите его здесь: '
        new_word = input(newkey)

        if new_word != '' or len(new_word) > 2:
            voc[word] = new_word
            print(f'Слово {word} с переводом {new_word} внесено в словарь')
        else:
            print('Ничего не введено или слишком короткое слово')
            continue


# Сохранить словарь
with open('dict.dat', 'wb') as dump_out:
    pickle.dump(voc, dump_out)

print('До новых встреч!!!')


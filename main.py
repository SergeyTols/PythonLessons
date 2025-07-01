## ДЗ
# stop_list = [] - Вводить слова, вывести сплитом пронумерованную коллонку слов в алфавит порядке, кроме стопслов из списка
# убрать слова в конце с помощью множеств(?)
                #1
stop_words = ['ну', 'типо', 'короче']
temp = []
message = input('Введите сообщение: ')
lst = message.split()
for item in lst:
    if item not in stop_words:
        temp.append(item)
res = sorted(temp)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')

                #2
stop_words = ['ну', 'типо', 'короче']
stop_words = set(stop_words)
message = input('Введите сообщение: ')
lst = message.split()
res = sorted(set(lst) - stop_words)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')
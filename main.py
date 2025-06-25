# Iterable object
# len() - сколько элементов в объекте

a = 123456

length = len(str(a))

print(length)

word = input('введите слово длинее 4 букв: ')
if not word or len(word) < 4:
    print('вы ничего не ввели или слово короче 4')
else:
    print('в вашем слове "' + word + '"', len(word), 'букв')

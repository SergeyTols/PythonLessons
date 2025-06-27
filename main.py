# Таблица символов
# Две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код) - возвращает символ по Unicode-коду

# print({ord('☃')})
# print(chr(9731))

word = 'Python'
slovo = ''
keys = set()

for ch in word:
    keys.add(ord(ch))
print(keys)
for item in keys:
    slovo += (chr(item))
print(slovo)

# abc = 'алфавит' ; сдвиг на +3 буквы - ДЗ
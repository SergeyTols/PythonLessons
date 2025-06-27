cards = {3, 7, 'туз', 'валет', 10}
second_card = {'туз'}
hase_ace = False

while cards:
    card = cards.pop()
    if card == 'туз':
        cards.add(card)
        hase_ace = True
    else:
        print(card)
        if hase_ace and len(cards) == 1:
            break

# PEP8 - правила именования
# c, l, O, I - не должны использоваться в переменных

# Операции над множествами

a = {3, 5, 7}
b = {3, 5, 7, 9, 11}

# объединенае множеств
# c = a.union(b)
c = b | a
print(c)

# Пересечение
# c = a.intersection(b) # выбор одинаковых эл-тов
c = a & b
print(c)

# Разность
# c = b.difference(a) # есть в 1-м, нет во 2-м
c = b - a
print(c)

# Симметричная разность
c = a.symmetric_difference(b)  # есть только в одном из двух
# c = b ^ a
print(c)

c = a < b
print(c)

c = a == b
print(c)

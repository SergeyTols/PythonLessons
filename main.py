# Области видимости
# Пример как делать не надо

a = [1, 2]


def change_array():
    a[0] = 0


change_array()
print(a)

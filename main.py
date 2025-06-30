# Списки
# Имитация стека

N = 5

lst_books = []

for i in range(N):
    print(f'положь книгу {i + 1}')
    lst_books.append(i + 1)

print('---')

while lst_books:
    item = lst_books.pop()
    print(f'бери книгу {item}')

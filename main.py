## Списочные выражения (list comprehension)
## Вложенные списки
# table = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
N = 3
table = [[1] * N for _ in range(N)]
# обход 2-мерного списка (матрицы)
count = 1
for row in range(len(table)):
    for col in range(len(table[row])):
        table[row][col] = count
        # print(table[row][col])
        count += 1

print(table)

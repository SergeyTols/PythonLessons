# factorial
# N = 5
# fact = 1
#
# for i in range(1, N + 1):
#     fact *= i
# print(fact)
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}', end='\t')
#     print()
total = 0
total_success = 0
min_val = float('inf')
max_val = float('-inf')
# height = int(input('Введи рост: '))

# while height > 180 or height < 150:
while (num := int(input('Введите рост: '))) != -1:
    if 150 < num < 180:
        total_success += 1
        if min_val > num:
            min_val = num
        if max_val < num:
            max_val = num
    total += 1

print(f'Число кандидатов: {total}')
print(f'Число прошедших: {total_success}')
print(f'Минимальный рост: {min_val}')
print(f'Максимальный рост: {max_val}')

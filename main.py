# factorial
N = 5
fact = 1

for i in range(1, N + 1):
    fact *= i
print(fact)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()


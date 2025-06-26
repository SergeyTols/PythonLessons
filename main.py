height = int(input('Введи рост: '))

# while height > 180 or height < 150:
while not (150 < height < 180):
    print('не подходит')
    height = int(input('Введи рост: '))

print(f'{height} подходит')


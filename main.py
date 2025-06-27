# города
s = set()

# city = input('Назовите горлод: ')

while (city := input('Назовите горлод: ')) != '':
    if city in s:
        print('такой был')
    else:
        s.add(city)

print(f'было названо городов: {len(s)}')
for item in s:
    print('\t', item)
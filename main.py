# Циклы:
# while
# while <условие>:
#     команды
# for
counter = 0 # Обнуляем счетчик
# цикл из 5 итераций
while counter < 5:
    print(f'Итерация номер: {counter + 1}')
    #count = count + 1 # инкремент
    counter +=1 # инкремент (краткая запись)
print(f'Итого в count уже {counter}')
print('Обратный отсчет:')
while counter > 0:
    print(f'{counter}')
    counter -=1 # декремент (краткая запись)
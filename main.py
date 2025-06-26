print('Варианты:\n\tL - влево\n\tR -вправо\n\tF - прямо\n\t Q - выход')

while  True:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'Д' | 'д':
            print('Свернул вправо')


        case 'Q' | '' | '' | '':
            print()
            break
        case _:


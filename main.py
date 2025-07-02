# Области видимости
# Shadows name 'square' from outer scope # локальная переменная перекрывает глобальную внутри функции
PI = 3.14


def greet(name: str) -> None:
    print('Привет,', name)
    name = 'друг'
    print('Здравствуй,', name)


def square_area(length: int, width: int) -> None:
    """

    :param length:
    :param width:
    :return:
    """
    area = length * width
    print(f'Площадь площади = {area}')


def circle_length(radius):
    perimetr = 2 * PI * radius
    print(f'Длинна окружности с радиусом {radius} = {perimetr:.2f}')


def print_array(array: list) -> None:
    for item in array:
        print(item)


# def print_array(array: list) -> None:
#     for item in words:  # Использование внешних переменных внутри ф-ции крайне не рекомендуется
#         print(item)


def main():
    area = 'Дворцовая площадь'
    words = ['Привет', 'мир']
    greet('Петр')
    print('Давай встретимся, где', area)
    square_area(320, 240)
    print('Ну что? Встречаемсяб где', {area})
    circle_length(5)
    print_array(words)
    print_array(['a', 'b', 'c'])

main()



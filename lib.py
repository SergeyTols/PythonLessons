def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это библиотека, а исполняемый: main.py')


# print(__name__)

class Car:
    counter = 0  # Сеатичное свойство (счетчик машин)

    def __init__(self, brand='Noname', model='Nomodel', color='black'):
        self.brand = brand  # 'Skoda'
        self.model = model  # 'Octavia'
        self.color = color  # 'red'
        self.engine_on = False
        Car.counter += 1

    def start_engine(self) -> None:
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Двигатель не заведен, не едем')

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Sergey', age=1):
        # свойства (поля) класса
        self._name = name
        self._age = age

    # Setter
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некоректный возраст — ', new_age)

    # Getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name}, возраст - {self._age}')

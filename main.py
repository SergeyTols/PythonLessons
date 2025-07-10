# Duck type - утиная типизация (прочитать)
#
#
# ООП (polymorphism)
# method override; operator overloading
# полиморфизм - св-во кода работать с разными типами данных
# Функция isinstance() проверяет, является ли объект (первый аргумент)
#            экземпляром или подклассом класса classinfo (второй аргумент
# isinstance() -> True
# isinstance
#
# from lib import Student, Employee, Person

lst = list(range(1, 15))
# lst += ['f']

class Stat:
    def __init__(self, vals):
        self.values = vals[:]

    def is_all_int(self) -> bool:
        return all(isinstance(item, int) for item in self.values)

    def get_min(self):
        if self.is_all_int():
            return min(self.values)
        return None

    def get_max(self):
        if self.is_all_int():
            return max(self.values)
        return None

    def get_aver(self):
        if self.is_all_int():
            return sum(self.values) / len(self.values)
        return None


s = Stat(lst)
print(s.get_min())
print(s.get_max())
print(s.get_aver())
print(lst)



class Selector:
    def __init__(self, vals):
        self.values = vals[:]  # получаем копию

    def get_odd(self):
        return [x for x in self.values if x % 2]

    def get_even(self):
        return [x for x in self.values if x % 2 == 0]

s = Selector(lst)
print(s.get_odd())
print(s.get_even())
print(lst)

# people = [
#     Person('Sergey', 27),
#     Student('Дима','РГГМО'),
#     Employee('Витя','Авангард'),
# ]
#
#
# for person in people:
#     if isinstance(person, Student):
#         # print(person.get_univercity())
#     # elif isinstance(person, Employee):
#     #     print(person.get_company())
#     # else:
#         print(person.get_name())


# retern vs yield(возвращает значение, но не завершает работу; не создает лист, создает генератор)

def generate_list():
    for i in range(5):
        return i


def generate_list2():
    for i in range(5):
        yield i

array = generate_list()
lst = tuple(generate_list2())
print(array)
print(lst)

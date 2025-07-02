#   Оператор is применяем на практике

def print_array(array: list, start: int = None):
    if start > len(array):
        return
    if start is None:
        for i in array:
            print(i)
    else:
        for i in range(start, len(array)):
            print(array[i])


a = [1, 2, 3]
print_array(a, 1)

# my_refregirator = ['колбаса', 'сыр', 'масло']
# # his_refregirator = ['колбаса', 'сыр', 'масло']
#
# his_refregirator = my_refregirator
# my_refregirator += ['мясо']
# his_refregirator += ['хлеб']
# print(my_refregirator == his_refregirator)
# print(id(my_refregirator) == id(his_refregirator))
# print(his_refregirator)
# print(my_refregirator)
# temp = None
# print(type(temp))
# print(temp is None)

#   Словарь также изменяем, как и множество со списком
# d = {'a': 1}
# print(id(d))
# d['a'] += 1
# print(id(d))

# a = [0]
# print(id(a))
# a [0] += 1
# print(id(a))

# a = 1
# print(id(a))
# a += 1
# print(id(a))



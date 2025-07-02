#   Функция, как объект
#   передается в другие функции(функции высшего порядка)

def square(num):
    # return num ** 2
    return str(num ** 2)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(square, nums)
print(list(squares))
# print(squares)

# С помощью map сделать строками, с помощью join слить в 1



# words = ['В', 'этом', 'списке', 'останутся', 'слова', 'длинна', 'которых',
#          'больше', 'шести']
#
# result = list(filter(is_longer_six, words))
# print(result)


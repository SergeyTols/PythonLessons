# lst = list(range(10))
# for item in lst:
#     print(item, '-', item ** 2)
from operator import truediv

# lst = list(range(10))
# # slice = lst[:len(lst):2]
# sl = lst[::2]
# print(sl)
# for item in range(0, len(lst), 2):
#     print(item, '-', item ** 2)

# lst = list(range(10))
# del lst[2]
# print(lst)
# del lst[::2]
# print(lst)

# lst = list(range(10))
# lst.pop()
# lst.pop(5)
# print(lst)

# lst = [1, 2, 2, 3, 4, 5]
# lst.remove(2)
# print(lst)

lst = [1, 7, 3, 5, 6, 4, 2]
lst.sort(reverse=True)
# lst.reverse()
print(lst)
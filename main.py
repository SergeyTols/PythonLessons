# for <переменная> in interable:

# word = 'поток'
#
# for ch in word:
#     print(ch)
#                  0      3     1
# итератор range(start, stop, step)

# for i in range(0,3,1):
#     print(i)

# for _ in range(5):
#     print("hi")

for i in range(0, 101):
    if i % 10 == 5:
        if i == 15:
            continue
        print(i)
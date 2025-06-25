a = 3
b = 5

temp = a
a = b
b = temp

print('До')
print('a =', a, 'b=', b)

a, b = b, a

print('после')
print(a, b)
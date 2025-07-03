

numbers = range(1,11)
squar = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(squar)

source_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}
dest_dict = {k: v * 2 for k, v in source_dict.items()}
print(dest_dict)
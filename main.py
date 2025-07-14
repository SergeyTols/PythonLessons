# JSON (Java Script object Notation)
# Для чтения:
# load() - читает из файла
# loads() - читает строковое представление
import json



with open('dogs.json', 'rt') as d:
    # data = json.load(d) # напрямую из файла
    temp = d.read() # читаем как строку
    data = json.loads(temp) # строковое представление JSON


for i in range(len(data)):
    print(f'Питомец № {i + 1}')
    for k, v in data[i].items():
        if type(v) == list:
            print(f'\t{k}: {', '.join(v)}')
        else:
            print(f'\t{k}: {v}')
# print(data)

# for k, v in data.items():
#     if type(v) == list:
#         print(f'{k}: {', '.join(v)}')
#     else:
#         print(f'{k}: {v}')

# print(json.dumps(data, indent=4))
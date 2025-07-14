# JSON (Java Script object Notation)
# Для чтения:
# load() - читает из файла
# loads() - читает строковое представление
import json



with open('dogs.json', 'rt') as d:
    data = json.load(d)

for k, v in data.items():
    if type(v) == list:
        print(f'{k}: {', '.join(v)}')
    else:
        print(f'{k}: {v}')

# print(json.dumps(data, indent=4))
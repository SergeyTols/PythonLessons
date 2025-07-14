# JSON (Java Script object Notation)
# Для чтения:
# load() - читает из файла
# loads() - читает строковое представление
import json



d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 120,
    'груша': 280,
}
# запись напрямую в файл
# with open('fruits.json', 'wt', encoding='utf-8') as f:
#     json.dump(d, f, indent=4)

# вывод в виде строки
data = json.dumps(d, indent=4)
print(data)
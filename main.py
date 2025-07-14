# CSV-файлы
import csv
from os import write

data = [
    ['name', 'age', 'city'],
    ['Борька', '25', 'Воронеж'],
    ['Влад', '75', 'Тверь'],
    ['Глеб', '35', 'Краснодар'],
]

with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
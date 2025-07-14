# CSV-файлы

import csv

from urllib3.filepost import writer

# with open('people.csv', 'r', encoding='utf-8') as f:
#     dict_reader = csv.DictReader(f)
#     for row in dict_reader:
#         print(f'{row['name']} живет в городе {row['city']}')

# Режимы квотирования
data = ['name', 25, 'town']
with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)

# field_names = ['name','age','city']
# data = {
#     'name' : 'Борька',
#     'age' : 27,
#     'city' : 'Москва'
# }
#
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writerow(data)
# data = [
#     ['name', 'age', 'city'],
#     ['Борька', '25', 'Воронеж'],
#     ['Влад', '75', 'Тверь'],
#     ['Глеб', '35', 'Краснодар'],
# ]
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
#
# with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
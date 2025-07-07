# Ctrl + Alt + o - убрать лишний импорт
# Документы (электронные таблицы)
# Excel (openpyxl)  pip install openpyxl
# pip freeze > requirements.txt

# Запись данных в существующий файл
from openpyxl import load_workbook

# открывавем рабочую книгу
wb = load_workbook('docs/report.xlsx')

# Активный лист
ws = wb.active
# можно по имени
# ws = wb['Отчет']

# Заголовки
ws['A1'] = 'ФИО'
ws['B1'] = 'Должность'
ws['C1'] = 'Отдел'

# Данные
employees = [
    ['Иванов И.И.', 'Менеджер', 'Продажи'],
    ['Петров П.П.', 'Бухгалтер', 'Финансы'],
    ['Сидорова С.С.', 'Аналитек', 'IT'],
]

for row, data in enumerate(employees, start=2):
    ws.cell(row=row, column=1, value=data[0])
    ws.cell(row=row, column=2, value=data[1])
    ws.cell(row=row, column=3, value=data[2])

wb.save('docs/employees.xlsx')


# способы записи
# ws['F1'] = 'Привет мир'
# ws.cell(row=1, column=3, value='Hello')

# wb.save('docs/newtable.xlsx')


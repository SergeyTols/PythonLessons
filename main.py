# Ctrl + Alt + o - убрать лишний импорт
# Документы (электронные таблицы)
# Excel (openpyxl)  pip install openpyxl
# pip freeze > requirements.txt
from turtledemo.penrose import start

# Чтение данных
from openpyxl import load_workbook

wb = load_workbook('docs/employees.xlsx')
ws = wb.active

rows_count = ws.max_row # Число заполненных строк

for row in ws.iter_rows(values_only=True):
    fio, pos, dept = row
    print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dept}')

# ws['A1'] = "=SUM(A1:A10)"

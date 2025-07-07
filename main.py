# Ctrl + Alt + o - убрать лишний импорт
# Документы (электронные таблицы)
# Excel (openpyxl)  pip install openpyxl
# pip freeze > requirements.txt

# Пустой Exel-файл
from openpyxl import Workbook

wb = Workbook() # wb - Workbook

ws = wb.active
ws.title = 'Отчет'

wb.save('docs/report.xlsx')

# Ctrl + Alt + o - убрать лишний импорт
# Документы
# pip install python-docx-template | pip install docxtpl
# pip freeze > requirements.txt
from itertools import count

from docxtpl import DocxTemplate

# # Загрузка шаблона
# doc = DocxTemplate('docs/template.docx')
#
# # Данные для подстановки в шаблон
# content = {
#     'company': 'ООО "Монолит"',
#     'employee': 'Петров Д.И.',
#     'position': 'Менеджер',
#     'date': '01/01/2025'
# }
#
# doc.render(content)
# doc.save('docs/about.docx')

# Загрузка шаблона
doc = DocxTemplate('docs/template.docx')

# Данные для подстановки в шаблон
content = [
    {
    'company': 'OOO "Монолит"',
    'employee': 'Петров Д.И.',
    'position': 'Менеджер',
    'date': '01/01/2025'
    },
    {
'company': 'OOO "Арсенал"',
    'employee': 'Петров Д.И.',
    'position': 'Менеджер',
    'date': '01/01/2025'
    }
]

count = 1
for item in content:
    doc.render(item)
    doc.save(f'docs/about{count}.docx')
    count +=1

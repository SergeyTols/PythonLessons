# Ctrl + Alt + o - убрать лишний импорт
# Документы
# pip install python-docx-template | pip install docxtpl
# pip freeze > requirements.txt
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
content = {
    'company': 'OOO "Монолит"',
    'employee': 'Петров Д.И.',
    'position': 'Менеджер',
    'date': '01/01/2025'
}

doc.render(content)
doc.save('docs/about.docx')
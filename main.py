# Ctrl + Alt + o - убрать лишний импорт
# Документы
# pip install python-docx
# pip freeze > requirements.txt
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Inches, Mm, Pt # Для размеров

doc = Document() # Создание экземпляра документа

# Добавление заголовка
doc.add_heading('Отчёт за месяц', 1)
paragr = doc.add_paragraph() # начать новый абзац
paragr = doc.add_paragraph('В этом отчете представлены')
# run - что-то внутри абзаца
paragr.add_run(' ключевые показатели').bold = True # bold - жир
paragr = doc.add_paragraph()
paragr_format = paragr.paragraph_format
paragr_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

paragr = doc.add_paragraph('Первый пункт', style='List Bullet')
paragr = doc.add_paragraph('Второй пункт', style='List Bullet')

paragr = doc.add_paragraph('Первый пункт', style='List Number')
paragr = doc.add_paragraph('Второй пункт', style='List Number')

paragr = doc.add_paragraph()
# Добавляем таблицу
table = doc.add_table(rows=3, cols=3)
# заполняем
for i, row in enumerate(table.rows):
    for j, cell in enumerate(table.columns):
        cell.text = f'Строка {i + 1}, Столбец {j + 1}'

doc.add_paragraph()
doc.add_picture('images/deep_blue.jpg', width=Mm(105)) # Добавили картинку

doc.save('docs/report.docx')


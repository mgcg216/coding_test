from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

document = Document()
font = document.styles['Normal'].font
font.name = 'Calibri'
section = document.sections[0]

sectPr = section._sectPr
cols = sectPr.xpath('./w:cols')[0]
cols.set(qn('w:num'),'4')

table = document.add_table(rows=1, cols=2)
table.style = 'Table Grid'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Amount'
hdr_cells[1].text = 'Serial'
for i in range(1000):
    row_cells = table.add_row().cells
    row_cells[0].text = str(i+1)
    row_cells[1].text = str(2*i)

document.save('demo.docx')
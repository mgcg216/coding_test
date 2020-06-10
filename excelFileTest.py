from openpyxl import Workbook

book = Workbook()

sheet = book.active

rows = ((1, 2, 3),
        (2, 3, 4),
        (4, 5, 6)
        )

for row in rows:
    sheet.append(row)

book.save("excelTest01.xlsx")
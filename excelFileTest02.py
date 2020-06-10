import openpyxl as op
book = op.load_workbook("excelTest01.xlsx")
sheetList = book.get_sheet_names()
# print(test)
sheet = book.get_sheet_by_name(sheetList[0]) # get a first sheet

rows = ((1, 2, 3),
        (2, 3, 4),
        (4, 5, 6)
        )

for row in rows:
    sheet.append(row)

book.save("excelTest01.xlsx")
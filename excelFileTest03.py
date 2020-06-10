import openpyxl as op
book = op.load_workbook("excelTest01.xlsx")
sheetList = book.get_sheet_names()
# print(test)
sheet = book.get_sheet_by_name(sheetList[0]) # get a first sheet

test = [501234]

sheet.append(test)

book.save("excelTest02.xlsx")
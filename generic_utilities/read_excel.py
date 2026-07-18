from xlrd import *

def read():
    wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\framework_DemoAppQspiders(M7)\\generic_utilities\\excel.xlsx")
    sheet=wb.sheet_by_name("Sheet1")
    row=sheet.row_values(1)               #['arbin','arbin@gmail.com',8687678]
    username=row[0]
    email=row[1]
    pwd=row[2]
    return username,email,pwd

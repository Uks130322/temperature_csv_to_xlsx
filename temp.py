import csv
from openpyxl import Workbook

data_rows = [fields for fields in csv.reader(open("temp_data_01.csv"))]

wb = Workbook()
ws = wb.active
ws.title = "Temperature data"
for row in data_rows:
    for index in range(len(row)):
        if row[index] == "Missing":
            row[index] = ""
        if row[index] and row[index][-1] == "%":
            row[index] = float(row[index][:-1]) / 100
    ws.append(row)

wb.save("temp_data_02.xlsx")

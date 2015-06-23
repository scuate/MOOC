##basic parsing of csv and xls files
import csv
import xlrd
DATAFILE = "beatles-diskography.csv"
DATAFILE2 = "beatles-1.xls"

def parse_file(datafile):
    data = []
    linenum = 0
    with open(datafile, "r") as f:
         reader = csv.DictReader(f)
         for row in reader:
             data.append(row)
    return data

parse_file(DATAFILE)

def xlparse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    print sheet.nrows
    print sheet.cell_type(1,0)
    print sheet.cell_value(2,3)
    print sheet.col_values(3, start_rowx=1,end_rowx=4)
    exceltime = sheet.cell_value(1,0)
    print "time:\n" + exceltime

xlparse_file(DATAFILE2)
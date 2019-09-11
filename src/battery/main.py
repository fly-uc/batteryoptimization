import csv
from cell import cell
#TODO: get motor import to work

def loadCSVIntoArray(path, objList):
    with open(path) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=';')
        lineCount = 0
        for row in csvReader:
            objList.append(cell(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[8]))

def main():
    cells = []
    loadCSVIntoArray('C:/Users/Keerthi Sekar/Documents/GitHub/batteryoptimization/src/battery/cellList.txt', cells)
    print(cells)

main()
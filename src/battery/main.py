import csv
import cell
#TODO: get motor import to work
class Test(object):
    def __init__(self, t1, t2, t3):
        self.col1 = t1
        self.col2 = t2
        self.col3 = t3

def loadCSVIntoArray(path):
    objList = []
    with open(path) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=';')
        lineCount = 0
        for row in csvReader:
            if lineCount == 1:
                newTest = Test(row[0],row[1],row[2])
                objList.append(newTest)
                print (newTest.toString())   
            lineCount += 1
    return objList

def main():
    motors = []
    motors = loadCSVIntoArray('C:/Users/Keerthi Sekar/Documents/GitHub/batteryoptimization/src/battery/motorTest.csv')
    print(motors)

main()


import csv
impoort cell.py


class pack:

        cellsInParallel = 0
        cellsInSeries = 0
        energyRequired = 0
        voltageRequired = 0
        powerRequired = 0
        additionalCapacity = 30
        cell = cell(0,0)
        cellList[]

    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.powerRequired = 0
        self.additionalCapacity = 30
        self.cell = cell(0,0)

    def setEnergyRequired(self, energy):
        self.energyRequired = energy
    
    def setVoltageRequired(self, voltage):
        self.voltageRequired = voltage

    def setPowerRequired(self,power):
        self.powerRequired = power
        
    def findPackConfig(self):
        self.cellsInSeries = voltageReqired/self.cell.getVoltage()
        self.cellsForCapacity = (self.energyRequired/((self.cell.getCapacity()-.7))*1.3 
        self.cellsForPower  = self.powerRequired/self.cell.getMaxDischarge()
    

    def loadCellInfo(self,path):
        with open('cellPortfolio.txt') as csv_file:
            csvReader = csv.reader(csv_file, delimiter=';')
            lineCount = 0
            for row in csvReader:
                if lineCount == 0:
                    #First line
                    #print(f'Column names are {", ".join(row)}')

                    lineCount += 1
                else:
                    #line 2 and after
                    #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    cell
                    lineCount += 1
                    


    def findCellsRequiredForPower(self, cell):
        

    def findCellsRequiredForVoltage(self,cell):
        

    def optimizePack(self):
        #Optimize pack for weight
    

    
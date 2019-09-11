

import csv
import cell

class pack(object):

    cellsInParallel = 0
    cellsInSeries = 0
    energyRequired = 0
    voltageRequired = 0
    powerRequired = [[]]
    additionalCapacity = 30
    totalCells = 0
    weightInKilograms = 0
    cell = cell(0,0)
    cellList = []

    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.currentRequired = 0
        self.peakCurrentRequired= 0
        self.additionalCapacity = 30
        self.cell = cell(0,0)

    def setEnergyRequired(self, energy):
        self.energyRequired = energy
    
    def setVoltageRequired(self, voltage):
        self.voltageRequired = voltage

    def setPowerRequired(self,powerInKW):
        #self.powerRequired = power
        self.powerRequired.append([])
        
    def powerRequiredFromCSV(self,path):
        with open(path) as csvFile:
            csvReader = csv.reader(csvFile,delimiter = ';')
            lineCount =  0
            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    #in this file, power is stored in the first column, and duration in second column
                    linecount += 1
                    self.powerRequired.append((row[0],row[1]))
                    
    #Rough estimate, shouldn't use
    def findBasicPackConfig(self,cell):
        self.cellsInSeries = self.voltageRequired/self.cell.getVoltage()
        self.cellsForCapacity = (self.energyRequired/((self.cell.getCapacity()-.7)))*1.3 
        self.cellsForPower  = self.powerRequired/self.cell.getMaxDischarge()
    
    #Gets cell info froma csv file
    def loadCellInfo(self,path):
        with open('cellList.txt') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            lineCount = 0
            for row in csvReader:
                if lineCount == 0:
                    #First line
                    print ('Cell Portfolio')
                    lineCount += 1
                else:
                    #line 2 and after
                    newCell = cell(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    self.cellList.append(newCell)
                    print (newCell.toString())
                    lineCount += 1
    
    #Gets a count of cells needed in parallel for power
    def findCellsRequiredForPower(self, cell):
        self.cellsInParallel = self.powerRequired/cell.getMaxDischarge()

    #Gets the count of cells required for voltage
    def findCellsRequiredForVoltage(self, cell):
        self.cellsInSeries = self.voltageRequired/cell.getVoltage()

    def findCellsRequiredForCapacity(self,cell):
        

    #finds total number of cells in a pack
    def findTotalCells(self):
        self.totalCells = self.cellsInParallel * self.cellsInSeries

    def findWeight(self):
        self.weightInKilograms = (self.totalCells * self.cell.getWeight)/1000

    def findThermalLosses(self):
        cellResistance = self.cell.getInternalResistance()
        parallelResistance = (self.cellsInParallel*(1/cellResistance))^-1
        overallResistance = self.cellsInSeries * parallelResistance
        energyLost = 0.0
        for element in self.energyRequired:
            energyLost += ((self.energyRequired[element][0]*self.energyRequired[element][1])*overallResistance^2)
        return energyLost

    def optimizePack(self):
        #Optimize pack for weight
        optimalCell = cell()
        cellIndex = 0

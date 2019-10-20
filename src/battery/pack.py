

import csv
from src.battery.cell import cell

class pack(object):

    cellsInParallel = 0
    cellsInSeries = 0
    energyRequired = 0
    voltageRequired = 0
    powerRequired = [[]]
    additionalCapacity = 30
    totalCells = 0
    weightInKilograms = 0
    cell = cell.emptyCell()
    cellList = []

    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.currentRequired = 0
        self.peakCurrentRequired= 0
        self.additionalCapacity = 30
        self.cell = cell.emptyCell()

    def setEnergyRequired(self, energy):
        self.energyRequired = energy
    
    def setVoltageRequired(self, voltage):
        self.voltageRequired = voltage

    def setPowerRequired(self,powerInKW):
        #self.powerRequired = power
        self.powerRequired.append([])
    
    def setAdditionalCapacity(self, percentage):
        self.additionalCapacity = percentage

    def setTotalCells(self, cellCount):
        self.totalCells = cellCount

    def setWeightInKilograms(self, weight):
        self.weightInKilograms = weight

    def setCell(self, newCell):
        self.cell = newCell

    def addCellToList(self, newCell):
        self.cellList.append(newCell)

    def getEnergyRequired(self):
        return self.energyRequired

    def getVoltageRequired(self):
        return self.voltageRequired
    
    def getPowerRequired(self):
        return self.powerRequired

    def getAdditionalCapacity(self):
        return self.additionalCapacity

    def getTotalCells (self):
        return self.totalCells

    def getWeight(self):
        return  self.weightInKilograms

    def getCell(self):
        return self.cell

    def getCellsInSeries(self):
        return self.cellsInSeries

    def getCellsInParallel(self):
        return self.cellsInParallel

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
                    self.energyRequired = self.energyRequired + ((row[0]*row[1])/(self.voltageRequired*1000))
                    
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
    def findCellsForPower(self, cell):
        return (self.powerRequired/cell.getMaxDischarge())

    #Gets the count of cells required for voltage
    def findCellsForVoltage(self, cell):
        return (self.voltageRequired/cell.getVoltage())

    def findCellsForCapacity(self,cell):
        return (self.energyRequired/cell.getCapacity())

    def findCellsInParallel(self, cell):
        if self.findCellsForPower(cell) > self.findCellsForCapacity(cell):
            self.cellsInParallel = self.findCellsForPower(cell)
        else:
            self.cellsInParallel = self.findCellsForCapacity(cell)
    
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

    def findDimensions(self):


    def optimizePack(self):
        #Optimize pack for weight
        optimalCell = self.cell
        previousWeight = 0
        self.setWeightInKilograms(0)

        for potentialCell in self.cellList:
            self.cell = potentialCell
            if previousWeight == 0:
                if self.getWeight() < previousWeight:
                    optimalCell = cell
                    previousWeight = self.getWeight

            



import csv
from src.battery.cell import cell


FLAGS_ENABLED = 1 #1 for warning messages, 0 to disable warnings
class pack(object):

    cellsInParallel = 0
    cellsInSeries = 0
    energyRequired = 0
    voltageRequired = 0
    powerRequired = [[]]
    additionalCapacity = 30
    totalCells = 0
    weightInKilograms = 0
    currentCell = cell.emptyCell()
    cellList = []
    
    #Default Constructor
    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.currentRequired = 0
        self.peakCurrentRequired= 0
        self.additionalCapacity = 30
        self.currentCell = cell.emptyCell()

    #Set energy spec
    def setEnergyRequired(self, energy):
        self.energyRequired = energy

    #Sets voltage spec
    def setVoltageRequired(self, voltage):
        self.voltageRequired = voltage

    #Sets power spec
    def setPowerRequired(self,powerInKW):
        #self.powerRequired = power
        self.powerRequired.append([])
    
    #Sets capacity margin
    def setAdditionalCapacity(self, percentage):
        self.additionalCapacity = percentage

    #Sets total cell count
    def setTotalCells(self, cellCount):
        self.totalCells = cellCount

    #Sets weight battery pack weight
    def setWeightInKilograms(self, weight):
        self.weightInKilograms = weight

    #Sets cell 
    def setCell(self, newCell):
        self.currentCell = newCell

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
        if(FLAGS_ENABLED ==1):
            if(self.totalCells <= 0):
                print('Function: getTotalCells in pack -  Warning: cell count is incorrect')
        return self.totalCells

    def getWeight(self):
        if(FLAGS_ENABLED)
        return  self.weightInKilograms

    def getCell(self):
        return self.currentCell

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
        if(FLAGS_ENABLED == 1):
            if(self.voltageRequired <= 0 ):
                print('Error -- Function: findBasicPackConfig() -- member of class pack  -- Voltage required has to be greater than 0')
            if(self.energyRequired <= 0):
                print('Error --  Function: findBasicPackConfig() -- member of class pack -- Energy Required has to be greater than 0')
            if(self.currentCell.getCapacity <= 0):
                print('Error -- Function: findBasicPackConfig() -- member of class pack -- Cell capacity must be greater than 0')
            if(self.powerRequired <= 0):   
                print('Error: -- Function: findBasicPackConfig() -- member of class pack -- power Required must be greater than 0')
            if(self.currentCell.getVoltage() <= 0):
                print('Error: -- Function findBasicPackConfig() -- member of class pack -- current cell voltage should be greater than 0')
            if(self.currentCell.getCapacity() <= 0):
                print('Error -- Function findBasicPackConfig() -- member of class pack -- current cell capacity should be greater than 0')
            if(self.currentCell.getMaxDischarge() <= 0):
                print('Error -- Function findBasicPackConfig() -- member of class pack  -- current cell max current dischange should be greater than 0')

        self.cellsInSeries = self.voltageRequired/self.currentCell.getVoltage()
        self.cellsForCapacity = (self.energyRequired/((self.currentCell.getCapacity()-.7)))*1.3 
        self.cellsForPower  = self.powerRequired/self.currentCell.getMaxDischarge()
    
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
        if(FLAGS_ENABLED == 1):
            if(self.powerRequired <= 0):
                print('Error -- Function findCellsForPower() -- member of class pack -- pack power required should be greater than 0')
            if(cell.getMaxDischarge() <= 0):
                print('Error -- Function findCellsForPower() -- member of cell pack -- cell max current dischange should be greater than 0')

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
        self.weightInKilograms = (self.totalCells * self.currentCell.getWeight)/1000

    def findThermalLosses(self):
        cellResistance = self.currentCell.getInternalResistance()
        parallelResistance = (self.cellsInParallel*(1/cellResistance))^-1
        overallResistance = self.cellsInSeries * parallelResistance
        energyLost = 0.0
        for element in self.energyRequired:
            energyLost += ((self.energyRequired[element][0]*self.energyRequired[element][1])*overallResistance^2)
        return energyLost

    def findDimensions(self,cell):
        #this is where all calculations are done for each pack
        self.findCellsInParallel(cell)
        self.findCellsForVoltage(cell)
        self.findThermalLosses()
    
    def optimizePack(self):
        #Optimize pack for weight
        optimalCell = self.currentCell
        previousWeight = 0
        self.setWeightInKilograms(0)

        for potentialCell in self.cellList:
            self.currentCell = potentialCell
            if previousWeight == 0:
                if self.getWeight() < previousWeight:
                    optimalCell = cell
                    previousWeight = self.getWeight

            

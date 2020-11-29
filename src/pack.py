#file --pack.py--
FLAGS_ENABLED = 1


from cell import cell
import math

class pack(object):

    cellsInParallel = 0
    cellsInSeries = 0
    energyRequired = 0
    packEnergyList = [[50000,.017],[40000, .067], [12250, .33]]
    voltageRequired = 0
    powerRequired = 0
    additionalCapacity = 30
    totalCells = 0
    weightInKilograms = 0
    currentCell = cell('empty',-1,-1,-1,-1,-1,-1,200000)
    #cell(name,ratedvoltage,capacity, peakContinousCurrent,startingVoltage,endingVoltage,resistance,weight)
    cellList = [cell('ICR18650_1',3.7,1600,1.6,3.7,2.7,.060,33),
    cell('ICR18650_2',3.7,1800,1.8,3.7,2.7,.060,39.5),
    cell('ICR18650_3',3.7,2000,1.8,3.7,2.7,.060,44.5),
    cell('ICR18650_4',3.7,2200,1.8,3.7,2.7,.060,46),
    cell('Li2x4p25RT',3.6,20000,360,3.6,2.7,.060,427),
    cell('Samsung', 3.6, 2500, 35 ,3.6,2.7, .060, 45),
    cell('Sony', 3.6, 3000, 30, 3.6, 2.7, .060, 46.6)]

    
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
    def setVoltageRequired(self, myVoltage):
        self.voltageRequired = myVoltage

    #Sets power spec
    def setPowerRequired(self,powerInKW):
        self.powerRequired = powerInKW
    
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
        if(FLAGS_ENABLED ==  1):
            if(self.energyRequired <= 0):
                print('Warning: Function getEnergyRequired() -- member of class pack -- enerrgyRequried should be greater than 0')
        return self.energyRequired

    def getVoltageRequired(self):
        if(FLAGS_ENABLED == 1):
            if(self.voltageRequired <= 0):
                print('Warning: Function getVoltageRequired() -- member of class pack -- voltageRequired should be greater than 0')
        return self.voltageRequired
    
    def getPowerRequired(self):
        if(FLAGS_ENABLED == 1):
            if(self.getPowerRequired <= 0):
                print('Warning: Function getPowerRequired() -- member of class pack -- power requried should be greater than 0')
        return self.powerRequired

    def getAdditionalCapacity(self):
        return self.additionalCapacity

    def getTotalCells (self):
        if(FLAGS_ENABLED ==1):
            if(self.totalCells <= 0):
                print('Function: getTotalCells in pack -  Warning: cell count is incorrect')
        return self.totalCells

    def getWeight(self):
        if(FLAGS_ENABLED == 1):
            if(self.weightInKilograms <= 0):
                print('Warning: -- Function getWeight() -- member of class pack -- weightInKilograms is less than or equal to 0')

        return  self.weightInKilograms

    def getCell(self):
        return self.currentCell

    def getCellsInSeries(self):
        return self.cellsInSeries

    def getCellsInParallel(self):

        return self.cellsInParallel

    #Gets capacity in Ah
    def getCapacity(self):
        if(FLAGS_ENABLED == 1):
            if(self.cellsInParallel <= 0):
                print('Error -- Function: getCapacity() --  member of class pack -- cells in parallel should be greater than 0')
            if(self.currentCell.getCapacity() <= 0):
                print('Error -- Function: getCapacity() -- member of class pack -- cell capacity should be greagter than 0')
        return ((self.cellsInParallel * self.currentCell.getCapacity())/1000)

    def powerRequiredFromCSV(self,path):
        '''
        with open(path) as csvFile:
            #csvReader = csv.reader(csvFile,delimiter = ';')
            lineCount =  0
            #for row in csvReader:
                #if lineCount == 0:
                   # lineCount += 1
                #else:
                    #in this file, power is stored in the first column, and duration in second column
                #    linecount += 1
                 #   self.powerRequired.append((row[0],row[1]))
                #    self.energyRequired = self.energyRequired + ((row[0]*row[1])/(self.voltageRequired*1000))

        '''

    def energyRequiredFromList(self, myList):
        if(FLAGS_ENABLED == 1):
            if(len(myList) == 0):
                print('Error -- Function: energyRequiredFromList() --  member of class pack -- No elements in list')
 
        totalEnergy = 0
        for power in myList:
            totalEnergy += (power[0]*power[1])
        self.energyRequired = totalEnergy
        
    #Rough estimate, shouldn't use
    def findBasicPackConfig(self,cell):
        if(FLAGS_ENABLED == 1):
            if(self.voltageRequired <= 0 ):
                print('Error -- Function: findBasicPackConfig() -- member of class pack  -- Voltage required has to be greater than 0')
            if(self.energyRequired <= 0):
                print('Error --  Function: findBasicPackConfig() -- member of class pack -- Energy Required has to be greater than 0')
            if(self.currentCell.getCapacity() <= 0):
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
        '''
        with open('cellList.txt') as csvFile:
            #csvReader = csv.reader(csvFile, delimiter=';') 
            lineCount = 0
            for row in csvReader:
                if lineCount == 0:
                    #First line
                    print ('Cell Portfolio')
                    lineCount += 1
                else:
                    #line 2 and after
                    #newCell = cell(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    #self.cellList.append(newCell)
                    #print (newCell.toString())
                    lineCount += 1
        '''
    
    #Gets a count of cells needed in parallel for power
    def findCellsForPower(self, myCell):
        if(FLAGS_ENABLED == 1):
            if(self.powerRequired <= 0):
                print('Error -- Function findCellsForPower() -- member of class pack -- pack power required should be greater than 0')
            if(myCell.getMaxDischarge() <= 0):
                print('Error -- Function findCellsForPower() -- member of cell pack -- cell max current dischange should be greater than 0')
            
            maxFlightCurrent = 0
            bustCurrent = self.powerRequired

            for element in self.packEnergyList:
                temp = element[0]/(self.cellsInSeries*self.currentCell.getVoltage())
                if(temp > maxFlightCurrent):
                    maxFlightCurrent = temp #safety factor

        return math.ceil((maxFlightCurrent/myCell.getMaxDischarge()))
    #Gets the count of cells required for voltage
    def findCellsForVoltage(self, myCell):
        if(FLAGS_ENABLED == 1):
            if(self.voltageRequired <= 0):
                print('Error  -- Function findCellsForVoltage() -- member of class pack  -- pack voltage required must be greater than 0')
            if(myCell.getVoltage() <= 0):
                print('Error -- Function findCellsForVoltage() -- member of class pack -- cell voltage must be greater than 0')
        
        return math.ceil((self.voltageRequired/myCell.getVoltage()))

    def findCellsForCapacity(self,cell):
        if(FLAGS_ENABLED == 1):
            if(self.energyRequired <= 0):
                print('Error -- Function findCellsForCapacity() -- member of class pack -- pack energy required must be greater than 0')
            if(cell.getCapacity() <= 0):
                print('Error -- Funciton findCellsForCapacity() -- member of class pack -- cell capacity must be greater than 0')

        return math.ceil((self.energyRequired/cell.getCapacity()))

    def findAdditionalCellsForCapacity(self, cell, capacity):
        return math.ceil((capacity/cell.getCapacity()))

#TODO: Consistancy issue, no return while findCellsInSeries() returns int 
    def findCellsInParallel(self, myCell):
        if self.findCellsForPower(myCell) > self.findCellsForCapacity(myCell):
            self.cellsInParallel = self.findCellsForPower(myCell)
        else:
            self.cellsInParallel = self.findCellsForCapacity(myCell)
    
    #finds total number of cells in a pack
    def findTotalCells(self):
        if(FLAGS_ENABLED == 1):
            if(self.cellsInParallel <= 0):
                print('Error -- Function findTotalCells() -- member of class pack -- cells in parallel must be greater than 0')
            if(self.cellsInSeries <= 0): 
                print('pack -- cells in series must be greater than 0')
        self.totalCells = self.cellsInParallel * self.cellsInSeries

    def findWeight(self):
        if(FLAGS_ENABLED == 1):
            if(self.totalCells <= 0):
                print('Error -- Function findWeight() -- member of class pack -- total cells must be greater than 0')
            if(self.currentCell.getWeight() <= 0):
                print('Error -- Function findWeight() -- member of class pack -- cell must have weight greater than 0')
        self.weightInKilograms = ((self.totalCells * self.currentCell.getWeight())/1000)

    def findThermalLosses(self):
        cellResistance = 0
        parallelResistance = 0
        overallResistance = 0
        
        if(FLAGS_ENABLED == 1):
            if(self.currentCell.getInternalResistance() < 0):
                print('Error -- Function findThermalLosses() -- member of class pack -- cell internal resistance unassigned')
            else:
                cellResistance = self.currentCell.getInternalResistance()
            if(self.cellsInParallel <= 0):
                print('Error -- Function findThermalLosses() -- member of class pack -- cells in parallel must be greater than 0')
            else:
                parallelResistance = 1/(self.cellsInParallel*(1/cellResistance))
            if(self.cellsInSeries <= 0):
                print('Error -- Function findThermalLosses() -- member of class pack -- cells in series must be greater than 0')
        
        overallResistance = self.cellsInSeries * parallelResistance
        
        energyLost = 0
        for element in self.packEnergyList:
            amps = element[0]/(self.cellsInSeries*self.currentCell.getVoltage())
            energyLost += ((amps**2)*overallResistance*element[1]) 
        return energyLost
     
    def findDimensions(self,myCell):
        #this is where all calculations are done for each pack
        self.cellsInSeries = self.findCellsForVoltage(myCell)
        self.findCellsInParallel(myCell)
        self.findTotalCells()
        additionalCapacity = self.findThermalLosses() #TODO: Technically additional energy
        additionalAmpHours = additionalCapacity/(self.currentCell.getVoltage()*self.cellsInSeries)
        additionalCellsInParallel = self.findAdditionalCellsForCapacity(self.currentCell,additionalAmpHours)
        self.cellsInParallel = self.cellsInParallel + additionalCellsInParallel
        self.findTotalCells()
        self.findWeight()

    def convertToBTU(self, wattHours):
        return (wattHours*3.412)

    def printPack(self):
        #print (f'Pack energy(KWh):')
        print('')
        voltage = self.getCellsInSeries()*self.currentCell.getVoltage()
        print(f'Pack voltage(V): {voltage}')
        print (f'Pack max continuous current(A): {(self.getCellsInParallel()*self.currentCell.getMaxDischarge())}')
        print (f'Cell name: {self.currentCell.getCellName()}')
        print(f'Cells in series: {self.cellsInSeries}')
        print(f'Cells in parallel: {self.cellsInParallel}')
        print(f'Total cells: {self.getTotalCells()}')
        print(f'Total capacity(Ah): {self.getCapacity()}')
        totalEnergy = (voltage*self.getCapacity())/1000
        print(f'Total energy(kWh): { totalEnergy }')
        print(f'Weight(Kg): {self.getWeight()}')
        thermalLoss = self.findThermalLosses()
        print(f'Thermal loss(Wh): {thermalLoss}')
        print(f'Thermal loss(BTU): {self.convertToBTU(thermalLoss)}')
        print ('_______________________________________________________________')

    def optimizePack(self):
        #Optimize pack for weight
        optimalCell = cell('empty',-1,-1,-1,-1,-1,-1,200000)
        previousWeight = 200000
        self.setWeightInKilograms(0)
        DISPLAY_OPTIMAL_ONLY = 0
        for potentialCell in self.cellList:
            self.currentCell = potentialCell
            self.findDimensions(self.currentCell)
            if self.getWeight() < previousWeight:
                optimalCell = self.currentCell
                previousWeight = self.getWeight()
                if(DISPLAY_OPTIMAL_ONLY == 0):
                    print('New optimal pack!')
            if(DISPLAY_OPTIMAL_ONLY == 0):
                self.printPack()
        self.currentCell = optimalCell
        self.findDimensions(self.currentCell)
        print('Optimal pack:')
        self.printPack()

    def findFeasiblePacks(self):
        #Needs to find cost
        print('Function is incomplete')

    def sortCellsByCost(self):
        print('Function is incomplete')
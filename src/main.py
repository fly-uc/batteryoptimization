

FLAGS_ENABLED = 1 #1 for warning messages, 0 to disable warnings

#Vehicle inputs:
motorCount = 8

#Motor input:
motorName = 'U7 V2.0 - KV 420'
motorVoltage =  25
motorMaxCurrent = 47.5


#Energy input:


class cell(object):

    #new cell
    cellName = 'empty'
    intitialPotential = -1
    finalPotential = -1
    ratedPotential = -1
    capacity = -1
    maxDischarge = -1
    internalResistance = -1
    remainingCapacity = -1 
    weight = -1
    usableCapacity = -1


    def __init__(self,cellName,ratedVoltage,capacity,peakCurrent,startingVoltage,endingVoltage,resistance,weight):
        self.cellName = cellName
        self.ratedPotential = ratedVoltage
        self.capacity = capacity
        self.maxDischarge = peakCurrent
        self.intitialPotential = startingVoltage
        self.finalPotential = endingVoltage
        self.internalResistance = resistance
        self.weight = weight
        self.remainingCapacity = capacity

    @classmethod
    def basicCell(self, ratedVoltage, maxAmperage):
        self.cellName = 'empty'
        self.intitialPotential = -1
        self.finalPotential = -1
        self.ratedPotential = -1
        self.capacity = -1
        self.maxDischarge = -1
        self.internalResistance = -1
        self.remainingCapacity = -1 
        self.weight = -1

    @classmethod
    def emptyCell(self):
        self.cellName = 'empty'
        self.intitialPotential = -1
        self.finalPotential = -1
        self.ratedPotential = -1
        self.capacity = -1
        self.maxDischarge = -1
        self.internalResistance = -1
        self.remainingCapacity = -1 
        self.weight = -1

    def cell_(self):
        self.cellName = ''
        self.initialPotential = 0
        self.finalPotential = 0
        self.capacity = 0
        self.maxDischarge = 0
        self.internalResistance = 0
        self.weight = 0 

    def setCellName(self, name):
        self.cellName = name

    def setInitialPotential(self, volts):
        self.intitialPotential = volts
   
    def setFinalPotential(self, volts):
        self.finalPotential = volts
   
    def setRatedPotential(self, volts):
        self.ratedPotential = volts
   
    def setCapacity(self, ampHours):
        self.capacity = ampHours
   
    def setMaxDischarge(self, amps):
        self.maxDischarge = amps
   
    def setInternalResistance(self,ohms):
        self.internalResistance = ohms
         
    def setWeight(self, grams):
        self.weight = grams

    def getCellName(self):
        return self.cellName

    def getWeight(self):
        return self.weight
   
    def getInitialPotential(self):
        return self.intitialPotential
   
    def getFinalPotential(self):
        return self.finalPotential
   
    def getMaxDischarge(self):
        return self.maxDischarge

    def getCapacity(self):
        return self.capacity

    def getInternalResistance(self):
        return self.internalResistance

    def findEnergyDensity(self):
        if(FLAGS_ENABLED == 1):
            if(self.capacity <= 0):
                print ('')

        energyDensity = self.capacity/self.weight
        return energyDensity

    def findPowerThermalLoss(self,I):
        power = (I^2)*self.internalResistance
        return power

    def findPowerDensity(self):
        #TODO: This will have to be done later, the discharge curve needs to be found with polynomial approximation
        return 0

    def findUsableCapacity(self):
        self.usableCapacity = self.capacity - self.remainingCapacity
    
    def findUsableEnergyDensity(self):
        #TODO: This will have to be done later, the discharge curve needs to be found with polynomial approximation
        return 0

    def toString(self):
        return (self.cellName + ', ' + self.ratedPotential + ', ' + self.capacity)


class motor(object):
    def __init__(self, name, motorType, current, voltage, torque, weight, RPM, iResistance):
        #max continuous currenet, voltage, torque, weight, rpm, internal resistance, operating temp, % throttle
        self.motorName = name
        self.motorType = motorType
        self.maxContinuousCurrent = current
        self.voltage = voltage
        self.torque = torque
        self.motorWeight = weight
        self.rpm = RPM
        self.internalResistance = iResistance
        self.operatingTemperature = 0
        self.percentThrottle = 0

    @classmethod
    def emptyMotor(self):
        #Sets all values to negative 1
        self.motorName = 'empty'
        self.motorType = -1
        self.maxContinuousCurrent = -1
        self.voltage = -1
        self.torque = -1
        self.motorWeight = -1
        self.rpm = -1
        self.internalResistance = -1
        self.operatingTemperature = -1
        self.percentThrottle = -1
    

    #set functions
    def setMotorName(self, name):
        self.motorName = name

    def setMotorType(self, motorType):
        self.motorType = motorType

    def setMaxContinuousCurrent(self, current):
        self.maxContinuousCurrent = current
    
    def setVoltage(self, voltage):
        self.voltage = voltage

    def setTorque(self, torque):
        self.torque = torque
    
    def setMotorWeight(self, weight):
        self.motorWeight = weight
    
    def setRPM(self, RPM):
        self.rpm = RPM

    def setInternalResistance(self, iResistance):
        self.internalResistance = iResistance
    
    def setOperatingTemperature(self, temperature):
        self.operatingTemperature = temperature
    
    def setPercentThrottle(self, percThrottle):
        self.percentThrottle = percThrottle

    #corresponding get functions
    def getMotorName(self):
        return self.motorName

    def getMotorType(self):
        return self.motorType

    def getMaxContinuousCurrent(self):
        return self.maxContinuousCurrent
    
    def getVoltage(self):
        return self.voltage

    def getTorque(self):
        return self.torque
    
    def getMotorWeight(self):
        return self.motorWeight
    
    def getRPM(self):
        return self.rpm

    def getInternalResistance(self):
        return self.internalResistance
    
    def getOperatingTemperature(self):
        return self.operatingTemperature
    
    def getPercentThrottle(self):
        return self.percentThrottle

    #TODO: write member functions to connect attributes

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
        if(FLAGS_ENABLED == 1):
            if(self.weightInKilograms <= 0):
                print('Error: ')

        return  self.weightInKilograms

    def getCell(self):
        return self.currentCell

    def getCellsInSeries(self):
        return self.cellsInSeries

    def getCellsInParallel(self):
        return self.cellsInParallel

    #Gets capacity in Ah
    def getCapacity(self):
        return ((self.cellsInParallel * self.currentCell.getCapacity)/1000)

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
    def findCellsForPower(self, cell):
        if(FLAGS_ENABLED == 1):
            if(self.powerRequired <= 0):
                print('Error -- Function findCellsForPower() -- member of class pack -- pack power required should be greater than 0')
            if(cell.getMaxDischarge() <= 0):
                print('Error -- Function findCellsForPower() -- member of cell pack -- cell max current dischange should be greater than 0')

        return (self.powerRequired/cell.getMaxDischarge())

    #Gets the count of cells required for voltage
    def findCellsForVoltage(self, cell):
        if(FLAGS_ENABLED == 1):
            if(self.voltageRequired <= 0):
                print('Error  -- Function findCellsForVoltage() -- member of class pack  -- pack voltage required must be greater than 0')
            if(cell.getVoltage() <= 0):
                print('Error -- Function findCellsForVoltage() -- member of class pack -- cell voltage must be greater than 0')
        
        return (self.voltageRequired/cell.getVoltage())

    def findCellsForCapacity(self,cell):
        if(FLAGS_ENABLED == 1):
            if(self.energyRequired <= 0):
                print('Error -- Function findCellsForCapacity() -- member of class pack -- pack energy required must be greater than 0')
            if(cell.getCapacity() <= 0):
                print('Error -- Funciton findCellsForCapacity() -- member of class pack -- cell capacity must be greater than 0')

        return (self.energyRequired/cell.getCapacity())

    def findCellsInParallel(self, cell):
        if self.findCellsForPower(cell) > self.findCellsForCapacity(cell):
            self.cellsInParallel = self.findCellsForPower(cell)
        else:
            self.cellsInParallel = self.findCellsForCapacity(cell)
    
    #finds total number of cells in a pack
    def findTotalCells(self):
        if(FLAGS_ENABLED == 1):
            if(self.cellsInParallel <= 0):
                print('Error -- Function findTotalCells() -- member of class pack -- cells in parallel must be greater than 0')
            if(self.cellsInSeries <= 0):
                print('Error -- Function findTotalCells() -- member of class pack -- cells in series must be greater than 0')
        self.totalCells = self.cellsInParallel * self.cellsInSeries

    def findWeight(self):
        if(FLAGS_ENABLED == 1):
            if(self.totalCells <= 0):
                print('Error -- Function findWeight() -- member of class pack -- total cells must be greater than 0')
            if(self.currentCell.getWeight() <= 0):
                print('Error -- Function findWeight() -- member of class pack -- cell must have weight greater than 0')
        self.weightInKilograms = ((self.totalCells * self.currentCell.getWeight())/1000)

    def findThermalLosses(self):
        
        if(FLAGS_ENABLED == 1):
            if(self.currentCell.getInternalResistance < 0):
                print('Error -- Function findThermalLosses() -- member of class pack -- cell internal resistance unassigned')
            if(self.cellsInParallel <= 0):
                print('Error -- Function findThermalLosses() -- member of class pack -- cells in parallel must be greater than 0')
            if(self.cellsInSeries):
                print('Error -- Function findThermalLosses() -- member of class pack -- cells in series must be graeater than 0')

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
        additionalCapacity = self.findThermalLosses()
        additionalCellsInParallel = (((additionalCapacity / self.voltageRequired)/self.currentCell.getCapacity())/1000)
        self.cellsInParallel = self.cellsInParallel + additionalCellsInParallel

    def printPack(self):
        #print (f'Pack energy(KWh):')
        print(f'Pack voltage(V): {(self.getCellsInSeries()*self.currentCell.getVoltage())}')
        print (f'Pack max continuous current(A): {(self.getCellsInParallel()*self.currentCell.getMaxDischarge())}')
        print (f'Cell name: {self.currentCell.getCellName()}')
        print(f'Cells in series: {self.cellsInSeries}')
        print(f'Cells in parallel: {self.cellsInParallel}')
        print(f'Total cells: {self.getTotalCells()}')
        print(f'Total capacity(Ah): {self.getCapacity()}')
        print(f'Weight(Kg): {self.getWeight()}')
        print(f'Thermal loss(Wh): {self.findThermalLosses()}')


    def optimizePack(self):
        #Optimize pack for weight
        optimalCell = self.currentCell
        previousWeight = 0
        self.setWeightInKilograms(0)

        for potentialCell in self.cellList:
            self.currentCell = potentialCell
            self.findDimensions(self.currentCell)
            self.printPack()
            if self.getWeight() < previousWeight:
                optimalCell = self.currentCell
                previousWeight = self.getWeight
                print('New optimal pack!')

        self.currentCell = optimalCell
        self.findDimensions(self.currentCell)
        print('Optimal pack:')
        self.printPack()

class vehicle(object):
    motorCount = -1
    #currentMotor  = motor()
    batteryPack = pack()
    motorList = []
    structuralMass = 0
    payloadMass = 0
    totalWeight = 0
    totalThrust = 0

    def __init__(self,motorCount,structuralMass, payloadMass):
        self.motorCount = motorCount
        self.structuralMass = structuralMass
        self.payloadMass = payloadMass

    def setMotorCount(self, numberOfMotors):
        self.motorCount = numberOfMotors

    def setMotor(self,motor):
        self.currentMotor = motor

    def setStructuralMass(self, mass):
        self.structuralMass = mass

    def setPayloadMass(self, mass):
        self.payloadMass = mass

    def setTotalWeight(self, mass):
        self.totalWeight = mass

    def getMotorCount(self):
        return self.motorCount

    def getMotor(self):
        return self.currentMotor
    
    def getStructualMass(self):
        return self.structuralMass

    def getPayloadMass(self):
        return self.payloadMass

    def getTotalWeight(self):
        return self.totalWeight

    def findTotalWeight(self):

        if(FLAGS_ENABLED == 1):
            if(self.structuralMass <= 0):
                print ('Warning: Invalid structural mass for vehicle')
            if(self.payloadMass <= 0):
                print ('Warning: Invalid payload mass for vehicle')
            if(self.batteryPack.getWeight() <= 0):
                print ('Warning: Battery pack weight is invalid')

        self.totalWeight = self.structuralMass + self.payloadMass + self.batteryPack.getWeight()

    #def openMotorList(self,path, motorList):
        #with open(path) as csvFile:
            #csvReader = csv.reader(csvFile, delimiter=';')
            #lineCount = 0
            #for row in csvReader:
                #motorList.append(motor(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))


#Main:





import math

FLAGS_ENABLED = 1 #1 for warning messages, 0 to disable warnings
DISPLAY_OPTIMAL_ONLY = 0 # 1 for displaying optimal cell only

#Vehicle inputs:
motorCount = 4
#Replit test
#example
#Motor input:
motorName = 'U7 V2.0 - KV 420'
motorVoltage =  25
motorMaxCurrent = 47.5

#Energy input:
#Format [power(Watts), duration(hours)],[power2(Watts), duration2(hours)]

energyList = [[8650,.00833],[5970,.5], [7040, .5], [3830,.00833]]

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
        return self

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

    def getVoltage(self):
        return self.ratedPotential

    def getMaxDischarge(self):
        return self.maxDischarge

    def getCapacity(self):
        return self.capacity

    def getInternalResistance(self):
        return self.internalResistance

    def findEnergyDensity(self):
        if(FLAGS_ENABLED == 1):
            if(self.capacity <= 0):
                print ('Warning -- Function findEnergyDensity() -- member of class cell -- Capacity must be greater than 0')

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
        if(FLAGS_ENABLED ==1):
            if(self.maxContinuousCurrent <= 0):
                print('Error -- Function: getMaxContinuousCurrent() -- member of class cell -- maxContinuousCurrent must be greater than  0')
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
    packEnergyList = energyList
    voltageRequired = 0
    powerRequired = 0
    additionalCapacity = 30
    totalCells = 0
    weightInKilograms = 0
    currentCell = cell('empty',-1,-1,-1,-1,-1,-1,200000)
    #cell(name,ratedvoltage,capacity, peakContinousCurrent,startingVoltage,endingVoltage,resistance,weight)
    cellList = [cell('Polymer Li-Ion 1055275',3.7,18000,42,3.7,2.7,.015,406.9),
     cell('Polymer Lithium-ion 9759156-10C cell',3.7,10000,100,3.7,2.75,.005,210),
     cell('LMP063767',3.8,3400,6.8,3.8,3,.018,29),
     cell('SLPB065070180',3.7,12000,24,3.7,2.7,.00204,1750),
     #cell('Licerion[experemental]',5,20000,60,5,4,.0018, 154),
     cell('UHP341440 NCA', 3.6,7500,150,3.6,2.7,.00065,320),
     #cell('553562-10C',3.7,1050,10,3.7,2.7,.04,18)
     cell('Venom Industrial LCO 22Ah',3.7,22000,330,3.7,3,.0002,415),
     cell('Venom Industrial LCO 16Ah',3.7,16000,240,3.7,3,.0002,300),
     cell('Venom Industrial LC0 13 Ah',3.7,13000,195,3.7,3,.0002,248),
     cell('Venom Industrial LCO 8 Ah', 3.7, 8000, 120, 3.7, 3, .0002, 167),
     cell('Venom Industrial LCO 37 Ah', 3.65, 37000, 120, 3.7, 3, .0003, 863),
     cell('SLPB98188216P', 3.7, 30000, 600, 3.7, 3, .0007, 780),
     cell('SLPB60216216', 3.7, 25000, 200, 3.7, 3, .0012, 555),
     cell('SLPB065070180', 3.7, 11600, 23.2, 3.7, 3, .0028, 175),
     cell('SLC-202', 3.7, 1750, 3.5, 3.7, 3, .001, 29)]
     #cell('553562-10C', 3.7, 1050, 10.5 ,3.7, 3, .001, 18),
     #cell('703562-10C', 3.7, 1150, 14, 3.7, 3, .001, 28)] #Cell options Licerion cell is experemental
    
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
        print(f'Pack voltage(V): {(self.getCellsInSeries()*self.currentCell.getVoltage())}')
        print (f'Pack max continuous current(A): {(self.getCellsInParallel()*self.currentCell.getMaxDischarge())}')
        print (f'Cell name: {self.currentCell.getCellName()}')
        print(f'Cells in series: {self.cellsInSeries}')
        print(f'Cells in parallel: {self.cellsInParallel}')
        print(f'Total cells: {self.getTotalCells()}')
        print(f'Total capacity(Ah): {self.getCapacity()}')
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
    '''
    def openMotorList(self,path, motorList):
        with open(path) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            lineCount = 0
            for row in csvReader:
                motorList.append(motor(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    '''

#Main:
myPack = pack()
myPack.setVoltageRequired(motorVoltage)
myPack.setPowerRequired((motorCount*motorMaxCurrent))
myPack.energyRequiredFromList(energyList)
print ('_______________________________________________________________')
myPack.optimizePack()


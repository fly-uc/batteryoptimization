
import csv

class motor(object):
    def __init__(self, name, motorType, current, voltage, torque, weight, RPM, iResistance, temperature, percThrottle):
        #max continuous currenet, voltage, torque, weight, rpm, internal resistance, operating temp, % throttle
        self.motorName = name
        self.motorType = motorType
        self.maxContinuousCurrent = current
        self.voltage = voltage
        self.torque = torque
        self.motorWeight = weight
        self.rpm = RPM
        self.internalResistance = iResistance
        self.operatingTemperature = temperature
        self.percentThrottle = percThrottle

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

    def getCurrent(self):
        return self.maxContinuousCurrent


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


    def __init__(self,cellName,ratedVoltage,capacity,peakCurrent,startingVoltage,endingVoltage,resistance,weight,remainingCapacity):
        self.cellName = cellName
        self.ratedPotential = ratedVoltage
        self.capacity = capacity
        self.maxDischarge = peakCurrent
        self.intitialPotential = startingVoltage
        self.finalPotential = endingVoltage
        self.internalResistance = resistance
        self.weight = weight
        self.remainingCapacity = remainingCapacity

    @classmethod
    def emptyCell(self, ratedVoltage, maxAmperage):
        self.cellName = 'empty'
        self.intitialPotential = -1
        self.finalPotential = -1
        self.ratedPotential = -1
        self.capacity = -1
        self.maxDischarge = -1
        self.internalResistance = -1
        self.remainingCapacity = -1 
        self.weight = -1

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

class pack(object):

    cellsInParallel = 0
    cellsInSeries = 0
    energyRequired = 0
    voltageRequired = 0
    powerRequired = [[]]
    additionalCapacity = 30
    totalCells = 0 
    weightInKilograms = 0
    
    cellList = []

    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.currentRequired = 0
        self.peakCurrentRequired= 0
        self.additionalCapacity = 30
        

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
k 
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
        self.cellsForPower  = self.peakCurrentRequired/self.cell.getMaxDischarge()
    
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
        return (self.powerRequired/cell.getMaxDischarge())

    #Gets the count of cells required for voltage
    def findCellsRequiredForVoltage(self, cell):
        return (self.voltageRequired/cell.getVoltage())

    def findCellsRequiredForCapacity(self,cell):
        return (self.energyRequired/cell.getCapacity())

    #finds total number of cells in a pack
    def findTotalCells(self):
        self.totalCells = self.cellsInParallel * self.cellsInSeries
        return self.totalCells

    def findWeight(self):
        self.weightInKilograms = (self.totalCells * self.cell.getWeight)/1000
        return self.weightInKilograms

    def findThermalLosses(self):
        cellResistance = self.cell.getInternalResistance()
        parallelResistance = (self.cellsInParallel*(1/cellResistance))^-1
        overallResistance = self.cellsInSeries * parallelResistance
        energyLost = (overallResistance^2) * self.peakCurrentRequired * 600
        print('Energy lost: ',energyLost, ' Watts')
        return energyLost
        
    def basicCalculations(self):
        self.cellsForPower = (self.findCellsRequiredForPower(self.cell)
        self.cellsForCapacity = (self.findCellsRequiredForCapacity(self.cell))
        self.cellsInSeries = (self.findCellsRequiredForVoltage(self.cell))

        if (self.cellsForPower < self.cellsForCapacity):
            self.cellsInParallel = self.cellsForCapacity
            print('Cells in parallel: ')
            print(self.cellsInParallel)
        else:
            self.cellsInParallel = self.cellsForPower
            print('Cells in parallel: ')
            print(self.cellsInParallel)

        energyLost = self.findThermalLosses()
        additionalParallelCells = ((energyLost/self.getVoltage())/.1)/((self.cell.getCapacity)/1000)
        print('Additional cells in parallel: ', additionalParallelCells)
        self.cellsInParallel = self.cellsInParallel + additionalParallelCells
        
#main
motorCount = 8
myMotor = motor('U11 TMotor','DC',57.3,48,4.33,.772,4583,0,0,100)
myBatteryCell = cell('Panasonic-Sayno',3.7,3700,15,3.6,3.5,.02,63,400)
myPack = pack()
myPack.setAdditionalCapacity(20)
myPack.setCell(myBatteryCell)
myPack.setEnergyRequired
myPack.setVoltageRequired(myMotor.getVoltage())
myPack.setPowerRequired((8*myMotor.getCurrent()))
myPack.basicCalculations()
print('Configuration')
print ('Series: ', myPack.getCellsInSeries())
print ('Parallel: ', myPack.getCellsInParallel())
print ('Total Cell Count: ', myPack.getTotalCells())
print ('Total Pack Weight: ',myPack.getTotalWeight(), ' kg')


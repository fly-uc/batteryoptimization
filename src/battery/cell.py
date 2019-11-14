
FLAGS_ENABLED = 1 #1 for warning messages, 0 to disable warnings
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
                print('Error -- Function findEnergyDensity() -- member of class pack -- pack capacity should be greater than 0')

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
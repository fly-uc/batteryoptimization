
class cell:
    def __init__(self, ratedVoltage, maxAmperage):
        self.cellName = 'generic cell'
        self.intitialPotential = -1
        self.finalPotential = -1
        self.ratedPotential = ratedVoltage
        self.capacity = -1
        self.maxDischarge = maxAmperage
        self.internalResistance = -1
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
        self.setCapacity = ampHours
    
    def setMaxDischarge(self, amps):
        self.maxDischarge = amps
    
    def setInternalResistance(self,ohms):
        self.internalResistance = ohms
    
    def setWeight(self, grams):
        self.weight = grams

    def getCellName(self):
        return self.cellName
    
    def getInitialPotential(self):
        return self.intitialPotential
    
    def getFinalPotential(self):
        return self.finalPotential
    
    def getMaxDischarge(self):
        return self.maxDischarge

    def getCapacity(self):
        return self.capacity

    def findEnergyDensity(self):
        energyDensity = self.capacity/self.weight
        return energyDensity

    def findPowerDensity(self):
        #TODO: This will have to be done later, the discharge curve needs to be found with polynomial approximation
        

    def findUsableCapacity(self):
        #TODO: This will have to be done later, the discharge curve needs to be found with polynomial approximation
        

    def findUsableEnergyDensity:
        #TODO: This will have to be done later, the discharge curve needs to be found with polynomial approximation

    
        


class cell:
    def __init__(self):
        self.cellName = 'generic cell'
        self.intitialPotential = -1
        self.finalPotential = -1
        self.ratedPotential =-1
        self.capacity = -1
        self.maxDischarge = -1
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

    def findEnergyDensity(self):
        energyDensity = self.capacity/self.weight
        return energyDensity

    def findPowerDensity(self):


    def findUsableCapacity(self):


    def findUsableEnergyDensity:
    

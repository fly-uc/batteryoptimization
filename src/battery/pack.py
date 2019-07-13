

class pack:

    def __init__(self):
        self.cellsInParallel = 0
        self.cellsInSeries = 0
        self.energyRequired = 0
        self.voltageRequired = 0
        self.powerRequired = 0
        self.additionalCapacity = 30
        self.cell = cell(0,0)
        
    def findPackConfig(self):
        self.cellsInSeries = voltageReqired/self.cell.getVoltage()
        cellsForCapacity = (self.energyRequired/((self.cell.getCapacity()-.7))*1.3 
        cellsForPower  = self.powerRequired/self.cell.getMaxDischarge()
        
    def optimizePack(self):
        #Optimize pack for weight
        

    
    


    
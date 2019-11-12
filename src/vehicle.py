from src.propulsion import motor.py
from src.battery import pack.py

class vehicle(object):
    motorCount = -1
    currentMotor = motor()
    batteryPack = pack()
    motorList[]
    self.structuralMass = 0
    self.payloadMass = 0

    def __init__(self,motorCount,structuralMass, payloadMass):
        self.motorCount = motorCount
        self.structuralMass = structuralMass
        self.payloadMass = payloadMass

    def setMotorCount(self, numberOfMotors):
        self.motorCount = numberOfMotors

    def setMotor(self,motor)
        self.currentMotor = motor

    def setStructuralMass(mass):
        self.structuralMass = mass

    def setPayloadMass(mass):
        self.payloadMass = mass

    def getMotorCount(self);
        return self.motorCount

    def getMotor(self):
        return self.currentMotor
    
    def getStructualMass(self):
        return self.structuralMass

    def getPayloadMass(self):
        return self.payloadMass

    def openMotorList(path, motorList):
        with open(path) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            lineCount = 0
            for row in csvReader:
                motorList.append(motor(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))


#main
def main():
    motorListPath = ''
    cellListPath = ''
    powerPath = ''

    


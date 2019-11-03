
from src.battery import pack.py
from src.propulsion import motor.py

class vehicle(object):
    motorCount = -1
    motor = motor()
    batteryPack = pack()
    motorCount = 0
    self.structuralMass = 0
    self.payloadMass = 0
    


    def __init__(self,motorCount,structuralMass, payloadMass):
        self.motorCount = motorCount
        self.structuralMass = structuralMass
        self.payloadMass = payloadMass

#main
def main():
    motorListPath = ''
    cellListPath = ''
    powerPath = ''

    


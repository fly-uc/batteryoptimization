#file --vehicle.py--

import src.cell
import src.motor
import src.pack

class vehicle(object):
    motorCount = -1
    batteryPack = pack()
    motorList = []
    structuralMass = 0
    payloadMass = 0
    totalWeight = 0
    totalThurst = 0

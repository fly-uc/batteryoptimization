#file --vehicle.py--

from cell import cell
from motor import motor
from pack import pack

class vehicle(object):
    motorCount = -1
    batteryPack = pack()
    motorList = []
    structuralMass = 0
    payloadMass = 0
    totalWeight = 0
    totalThurst = 0

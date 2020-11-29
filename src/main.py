#file --main.py--

from cell import cell
from motor import motor
from pack import pack
from vehicle import vehicle

#Vehicle inputs:
motorCount = 1
#example
#Motor input:
motorName = 'Emrax 228 MV'
motorVoltage =  300
motorMaxCurrent = 167.7

#Energy input:
#Format [power(Watts), duration(hours)],[power2(Watts), duration2(hours)]
powerInterval = [[50000,.017],[40000, .067], [12250, .33]] #FIXME: This doesn't assign correctly, set it in line 13 in pack.py

myPack = pack()
myPack.setVoltageRequired(motorVoltage)
myPack.energyRequiredFromList(powerInterval)
myPack.setPowerRequired(motorMaxCurrent*motorCount)
print('_______________________________________________________________')
myPack.optimizePack()
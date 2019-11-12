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

    @classmethod
    def emptyMotor(self):
        #Sets all values to negative 1
        self.motorName = 'empty'
        self.motorType = -1
        self.maxContinuousCurrent = -1
        self.voltage = -1
        self.torque = -1
        self.motorWeight = -1
        self.rpm = -1
        self.internalResistance = -1
        self.operatingTemperature = -1
        self.percentThrottle = -1
    

    #set functions
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

    #TODO: write member functions to connect attributes

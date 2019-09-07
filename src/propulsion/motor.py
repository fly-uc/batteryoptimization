
class motor:
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

def main():
    motor2 = motor("test", "DC", 1, 2, 3, 4, 5, 6, 7, 8)

if __name__ == "__main__":
    main()
class TemperatureExceededError(Exception):
    pass

class Sensor:

    def __init__(self,temperature):
        self._temperature = temperature

    def check_temperature(self):
        if self._temperature > 50 :
            raise TemperatureExceededError ('Temperature Too Hign')
        else :
            print('Normal Temperature')

sensor = Sensor(55)

try:
    sensor.check_temperature()
except TemperatureExceededError as  e:
    print(e)
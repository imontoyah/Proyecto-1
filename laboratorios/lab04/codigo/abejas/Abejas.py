import math
class Bee:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def toString(self):
        print(self.latitude, self.altitude, self.longitude) 



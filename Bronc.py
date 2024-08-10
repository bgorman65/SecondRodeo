from Animal import Animal

class Bronc(Animal):
    def __init__(self, earTag):
        super().__init__(earTag)
        self.straight = None
        self.flankTightness = None
        self.speed = None
        self.direction = None

    def setStraight(self, straight):
        self.straight = straight

    def getStraight(self):
        return self.straight

    def setFlankTightness(self, flankTightness):
        self.flankTightness = flankTightness

    def getFlankTightness(self):
        return self.flankTightness

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
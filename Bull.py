from Animal import Animal

class Bull(Animal):
    def __init__(self, earTag):
        super().__init__(earTag)
        self.straight = None
        self.speed = None
        self.direction = None

    def setStraight(self, straight):
        self.straight = straight

    def getStraight(self):
        return self.straight

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
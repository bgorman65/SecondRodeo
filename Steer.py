from Animal import Animal

class Steer(Animal):
    def __init__(self, earTag):
        super().__init__(earTag)
        self.stop = None
        self.speed = None
        self.direction = None

    def setStop(self, stop):
        self.stop = stop

    def getStop(self):
        return self.stop

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
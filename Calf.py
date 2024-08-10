from Animal import Animal

class Calf(Animal):
    def __init__(self, earTag):
        super().__init__(earTag)
        self.kick = None
        self.speed = None
        self.direction = None

    def setKick(self, kick):
        self.kick = kick

    def getKick(self):
        return self.kick

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
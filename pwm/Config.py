class Config:
    def __init__(self, version, system, windowSize):
        self.version = version
        self.system = system
        self.windowSize = windowSize

    def Test():
        print("Config is Running")


    def getVersion(self):
        return self.version 

    def getSystem(self):
        return self.system

    def getWindowSize(self):
        return self.windowSize

    def setVersion(self, input):
        self.version = input

    def setSystem(self, input):
        self.system = input

    def setWindowSize(self, input):
        self.windowSize = input


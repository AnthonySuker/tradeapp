class stockObject:
    algoVars = {}
    high = []
    low = []
    vol = []
    close = []

    def __init__ (self):
        print("Created Base Object")

    def importHigh(self, data):
        self.high = data

    def importLow(self, data):
        self.low = data

    def importClose(self, data):
        self.close = data

    def importVol(self, data):
        self.Vol = data

    def applyAlgo(self):
        print("Base algorithm")



### Child Stratagies ###

class VolumeSpike(stockObject):
    def applyAlgo(self):
        print("doing stuff")
        #if volume has increased by x% since last check
        # & price has changed positively
        #return true with confidence
        


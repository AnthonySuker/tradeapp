import yfinance as yf

def tttt():
    print('tttt')

class stockChecker:
    algoVars = {}
    high = []
    low = []
    vol = []
    close = []        
    
    def __init__ (self,name):
        print("Created Base Object")
        ticker = yf.Ticker(name)
        hist = ticker.history(period='max')
        self.high = hist['High']
        self.low = hist['Low']
        self.vol = hist['Volume']
        self.close = hist['Close']
        
    def printData():
        print(self.high)
        print(self.low)
        print(self.vol)
        print(self.close)
    
    def applyAlgo(self):
        print("Base algorithm")
        


### Child Stratagies ###

class VolumeSpike(stockChecker):
    def applyAlgo(self):
        print("doing stuff")
        #if volume has increased by x% since last check
        # & price has changed positively
        #return true with confidence


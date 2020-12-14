import yfinance as yf
class stock:
    high = []
    low = []
    vol = []
    close = []        
    
    def __init__ (self,name):
        print("Creating Tracker...",end='')
        ticker = yf.Ticker(name)
        hist = ticker.history(period='max')
        self.high = hist['High']
        self.low = hist['Low']
        self.vol = hist['Volume']
        self.close = hist['Close']
        print("Complete!")
        
    def printData(self):
        print("printing data")
        print(self.high)
        print(self.low)
        print(self.vol)
        print(self.close)

    def getData(self):
        return self.high, self.low, self.vol, self.close
    
    def applyAlgo(self):
        print("Base algorithm")


trackedDict = {}


def createNewTracker(stockID):
    if stockID in trackedDict.keys():
        return 'Stock already tracked'
    else:
        temp = stock(stockID)
        trackedDict[stockID] = temp

def printdata(stockID):
    print("TEST")
    trackedDict[stockID].printData()

def getStockData(stockID):
    t = trackedDict[stockID]
    return t.getData()
    

def getTracked():
    return trackedDict.keys()
import StockTracker as st
import sys
import numpy as np
import Algorithms as alg

np.set_printoptions(threshold=sys.maxsize)




print("```STOCK TRACKER```")

def addStock():
    stockID = input("Enter Stock ID: ")
    st.createNewTracker(stockID)

def printStockInfo():
    stockID = input("Enter Stock ID: ")
    temp = st.getStockData(stockID)
    print('0. All Data\n1. High\n2. Low\n3. Volume\n4. Close')
    x = int(input("enter: "))
    if x == 0:
        print(temp)
    else:
        print(temp[x-1])

def printTracker():
    print(st.getTracked())

# just change this to use what ever algorithm method you make.
# I'll create something later to choose which algo is used but not much point
# when mines the only one lol
def applyAlgo():
    stockID = input("Enter Stock ID: ")
    temp = st.getStockData(stockID)
    t = alg.Ichimoku(temp)
    t.graph()
    


methods = {
    1 : addStock,
    2 : printStockInfo,
    3 : printTracker,
    4 : applyAlgo
}

while True:
    print('0. Exit\n1. Add Stock\n2. Print Stock Info\n3. Print Tracked Stocks\n4. Apply Algorithm')
    opt = int(input())
    if opt == 0:
        print("Goodbye")
        break
    methods[opt]()
    print('\n################################################\n')

# p1 = stockChecker('CBA.AX')

# p1.printData()
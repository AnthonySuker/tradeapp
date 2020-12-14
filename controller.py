import StockTracker as st
import sys
import numpy as np

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


methods = {
    1 : addStock,
    2 : printStockInfo,
    3 : printTracker
}

while True:
    print('0. Exit\n1. Add Stock\n2. Print Stock Info\n3. Print Tracked Stocks')
    opt = int(input())
    if opt == 0:
        print("Goodbye")
        break
    methods[opt]()

# p1 = stockChecker('CBA.AX')

# p1.printData()
import numpy as np
import math

# This is the base class, shouldn't need to do much to it
# Just loads relevant data structures 
class baseAlgorithm:
    high = []
    low = []
    vol = []
    close = []   
    confidence = 50
    def __init__(self,data):
        self.high = data[0]
        self.low = data[1]
        self.vol = data[2]
        self.close = data[3]



# A really complex algorithm
# just checks the last 2 values of volume traded and gives a confidence based off that
# some say its the best trading algorithm ever invented
class volumeIncrease(baseAlgorithm):
    def run(self):
        if self.vol[-1] > self.vol[-2]:
            self.confidence = 100
        else:
            self.confidence = 0
        print("Algorithm Confidence is:",end=' ')
        print(self.confidence)

# in the algorithms you make you should keep this the same
# atleast the super line
# that runs its parent class (baseAlgorithm) initiliazation method which loads the data
# and then runs its own stuff

    def __init__(self,data):
        super(volumeIncrease, self).__init__(data)
        self.run()
    

#theres more comments in controller @ line 30


class Ichimoku(baseAlgorithm):
    def run(self):

        ##Deciding to buy, sell or stay
        conversion1 = (max(self.high[-9:] + max(self.low[-9:])))*0.5
        conversion2 = (max(self.high[-10:-1] + max(self.low[-10:-1])))*0.5
        if (conversion2 > self.close[-2]) and (conversion1 < self.close[-1]):
            self.order = 'Buy'
        if (conversion2 < self.close[-2]) and (conversion1 > self.close[-1]):
            self.order = 'Sell'


        ##This is a crude way of calculating a confidence but it will work for now
        spanA = (((max(self.high[-35:-26]) + max(self.low[-35:-26]))*0.5) + (max(self.high[-52:-26]) + min(self.low[-52:-26]))*0.5)*0.5

        spanB = (max(self.high[-78:-26]) + min(self.low[-78:-26]))*0.5

        self.confidence = ((100/math.pi)*math.atan(spanA-spanB))+50

        print("Algorithm Confidence is:",end=' ')
        print(self.confidence)


    ##This is from the example too
    def __init__(self,data):
        super(Ichimoku, self).__init__(data)
        self.run()



#IKH strategy for a long term investment

import numpy as np
import math


##Taken this straight from the example
class baseAlgorithm:
    high = []
    low = []
    vol = []
    close = []
    confidence = 50
    order = 'Stay'
    def __init__(self,data):
        self.high = data[0]
        self.low = data[1]
        self.vol = data[2]
        self.close = data[3]


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

        spanB = (max(self.high[-78:-26]) + min(self.low[-78-26]))*0.5

        self.confidence = ((100/math.pi)*math.atan(spanA-spanB))+50


    ##This is from the example too
    def __init__(self,data):
        super(Ichimoku, self).__init__(data)
        self.run()


## I hope this works, let me know if anything won't work and why it doesn't
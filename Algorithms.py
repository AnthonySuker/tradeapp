import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
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

    def graph(self):
        print('Base Algorithm reached')


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

    #this will be a graph of the last 100 days
    def graph(self):
        conversion_line = []
        base_line = []
        leading_span_a = []
        leading_span_b = []
        lagging_span = []
        length = len(self.high)

        marker = 0

        for i in range(length-100, length):
            conversion_line.append((max(self.high[i-9:i]) + max(self.low[i-9:i]))*0.5)
            base_line.append((max(self.high[i-26:i]) + min(self.low[i-26:i]))*0.5)
            leading_span_a.append((((max(self.high[i-9-26:i-26]) + max(self.low[i-9-26:i-26]))*0.5 \
            + (max(self.high[i-26-26:i-26]) + min(self.low[i-26-26:i-26]))*0.5))*0.5)
            leading_span_b.append((max(self.high[i-52-26:i-26]) + min(self.low[i-52-26:i-26]))*0.5)

            if marker > 26:
                lagging_span.append(close[i])

            marker += 1

        charts_dict = {
        "Conversion Line" : pd.Series(conversion_line), \
        "Base Line" : pd.Series(base_line), \
        "Leading Span A" : pd.Series(leading_span_a), \
        "Leading Span B" : pd.Series(leading_span_b), \
        "Lagging Span" : pd.Series(lagging_span), \
        }

        plt.plot(charts_dict['Leading Span A'],label='Leading Span A')
        plt.plot(charts_dict['Leading Span B'],label='Leading Span B')
        plt.plot(charts_dict['Conversion Line'], label='Conversion Line')
        plt.plot(range(0, 100), self.close[-100:],label='Close Price')
        plt.plot(charts_dict['Base Line'],label='Base Line')
        plt.plot(charts_dict['Lagging Span'],label='Lagging Span')
        plt.fill_between(range(0, 100), Ichimoku['Leading Span A'], Ichimoku['Leading Span B'], color='g')
        plt.legend()

        plt.show()


    ##This is from the example too
    def __init__(self,data):
        super(Ichimoku, self).__init__(data)
        self.run()



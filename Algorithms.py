import numpy as np

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
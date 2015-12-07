import random, math

# Base Model for all DTLZ
class Model(object):
    def gen(self):
        while True:
            for i in xrange(self.decisionsN):
                self.decisions[i] = random.uniform(self.bottom[i], self.top[i])
            if self.isValid(): 
                break

    def __init__(self):
        self.objectivesN, self.decisionsN = 0, 0
        self.decisions, self.prevDecision, self.objectives = [], [], []
        self.top, self.bottom = [0], [0]
        self.gen()

    def eval(self):
        return sum(self.getObjectives())

    def copy(self,other):
        self.decisionsN, self.objectivesN = other.decisionsN, other.objectivesN
        self.decisions, self.prevDecision, self.objectives = other.decisions[:], other.prevDecision[:], other.objectives[:]
        self.top, self.bottom = other.top[:], other.bottom[:]

    def getObjectives(self):
        return []

    def isValid(self):
        for i in xrange(0, self.decisionsN):
            if self.decisions[i] < self.bottom[i] or self.decisions[i] > self.top[i]:
                return False
        return True
        
# Specific DTLZ models
class DTLZ1(Model):
    def __init__(self, dec = 10, obj = 2):
        self.decisionsN, self.objectivesN = dec, obj
        self.decisions, self.prevDecision, self.objectives = [0 for x in xrange(dec)], [], []
        self.top, self.bottom = [1 for x in xrange(dec)], [0 for x in xrange(dec)]
        self.gen()

    def getObjectives(self):
        if self.prevDecision == self.decisions:
            return self.objectives
        
        obj = []

        y=self.decisionsN - self.objectivesN + 1
        for x in self.decisions[self.objectivesN - 1:]:
            y += pow(x - 0.5, 2) - math.cos((x - 0.5) * 20 * math.pi)

        y *= 100
        for i in xrange(self.objectivesN):
            t = 0.5 * (1 + y)
            for x in self.decisions[:self.objectivesN - i - 1]:
                t *= x
            
            if i != 0:
                t *= (1 - self.decisions[self.objectivesN - i])
            
            obj.append(t)
        
        self.prevDecision = self.decisions
        self.objectives = obj

        return obj

class DTLZ3(Model):
    def __init__(self, dec = 10, obj = 2):
        self.decisionsN, self.objectivesN = dec, obj
        self.decisions, self.prevDecision, self.objectives = [0 for x in xrange(dec)], [], []
        self.top, self.bottom = [1 for x in xrange(dec)], [0 for x in xrange(dec)]
        self.gen()

    def getObjectives(self):
        if self.prevDecision == self.decisions:
            return self.objectives

        obj = []

        y = self.decisionsN - self.objectivesN + 1
        for x in self.decisions[self.objectivesN-1:]:
            y += pow(x - 0.5, 2) - math.cos((x - 0.5) * 20 * math.pi)

        y *= 100
        for i in xrange(self.objectivesN):
            t = y + 1
            for x in self.decisions[:self.objectivesN - i - 1]:
                t *= math.cos(x * math.pi / 2)
            
            if i != 0:
                t *= math.sin(self.decisions[self.objectivesN - i] * math.pi / 2)
            
            obj.append(t)

        self.prevDecision = self.decisions
        self.objectives = obj

        return obj

class DTLZ5(Model):
    def __init__(self, dec = 10, obj = 2):
        self.decisionsN, self.objectivesN = dec, obj
        self.decisions, self.prevDecision, self.objectives = [0 for x in xrange(dec)], [], []
        self.top, self.bottom = [1 for x in xrange(dec)], [0 for x in xrange(dec)]
        self.gen()

    def getObjectives(self):
        if self.prevDecision == self.decisions:
            return self.objectives

        obj = []

        y = 0
        for x in self.decisions[self.objectivesN-1:]:
            y += pow(x - 0.5, 2)
        
        theta = [math.pi * self.decisions[0] / 2]
        for x in self.decisions[1:self.objectivesN - 1]:
            theta.append((1 + 2 * y * x) * math.pi / (4 * (1 + y)))
        
        for i in xrange(self.objectivesN):
            t = 1 + y
            for x in theta[:self.objectivesN - i - 1]:
                t *= math.cos(x * math.pi / 2)
            
            if i!= 0:
                t *= math.sin(theta[self.objectivesN - i - 1] * math.pi / 2)
    
            obj.append(t)

        self.prevDecision = self.decisions
        self.objectives = obj

        return obj

class DTLZ7(Model):
    def __init__(self, dec = 10, obj = 2):
        self.decisionsN, self.objectivesN = dec, obj
        self.decisions, self.prevDecision, self.objectives = [0 for x in xrange(dec)], [], []
        self.top, self.bottom = [1 for x in xrange(dec)], [0 for x in xrange(dec)]
        self.gen()

    def getObjectives(self):
        if self.prevDecision == self.decisions:
            return self.objectives

        obj = []
        
        y = 1 + 9/(self.decisionsN - self.objectivesN + 1) * sum(self.decisions[self.objectivesN - 1:])
        z = self.objectivesN
        
        for i in xrange(self.objectivesN - 1):
            obj.append(self.decisions[i])
            z -= obj[i] / (1 + y) * (1 + math.sin(3 * math.pi * obj[i]))

        obj.append((1 + y) * z)

        self.prevDecision=self.decisions
        self.objectives=obj

        return obj

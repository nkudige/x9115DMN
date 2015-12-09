from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

import sys

class Schaffer:
    def __init__(self, dec = 1, obj = 2):
                
        self.objectivesN, self.decisionsN = obj, dec
        self.decisions, self.prevDecision, self.objectives = [0 for x in xrange(dec)], [], []
        self.top, self.bottom = [pow(10,5)], [-pow(10,5)]
        
        self.gen()
        
        self.f1_low = -pow(10,10)
        self.f1_high = pow(10,10)
        self.f2_low = -pow(10,10)
        self.f2_high = pow(10,10)
        self.baseline_high = pow(10,10)
        self.baseline_low = -pow(10,10)
    
    def low(self, d):
        return self.bottom[d]
    
    def high(self, d):
        return self.top[d]
        
    def isValid(self):
        return False if self.decisions[0] > pow(10,5) or self.decisions[0] < -pow(10,5) else True
    
    def resetBaselines(self, rep = 1000000):
        f1low = f2low = sys.maxint
        f1high = f2high = -f1low
        low = sys.maxint
        high = -low
        for _ in xrange(0, rep):
            state = self.gen()
            state_energy = self.energy(state)
            f1_energy = self.f1(state)
            f2_energy = self.f2(state)
            
            f1high = f1_energy if f1_energy > f1high else f1high
            f1low = f1_energy if f1_energy < f1low else f1low
            
            f2high = f2_energy if f2_energy > f2high else f2high
            f2low = f2_energy if f2_energy < f2low else f2low
            
            high = state_energy if state_energy > high else high
            low = state_energy if state_energy < low else low

        self.baseline_low = low
        self.baseline_high = high
        self.f1_high = f1high
        self.f1_low = f1low
        self.f2_high = f2high
        self.f2_low = f2low
    
    def f1(self, x):
        return pow(x[0], 2)
    
    def f2(self, x):
        return pow((x[0]-2), 2)
        
    def eval(self):
        return sum(self.getObjectives())
        
    def energy(self, x):
        return self.f1(x) + self.f2(x)
    
    def aggregate_energy(self, x):
        return (sqrt(pow(self.normalize_energy(self.f1(x), self.f1_low, self.f1_high), 2) + pow(self.normalize_energy(self.f2(x), self.f2_low, self.f2_high), 2))/(sqrt(len(x))))
    
    def normalize_energy(self, energy, low, high):
        return (energy - low)/(high - low)
    
    def denormalize_energy(self, energy, low=None, high=None):
        low = low if low else self.baseline_low
        high = high if high else self.baseline_high
        
        return (high - low) * energy + low
    
    def gen(self):
        while True:
            for i in xrange(self.decisionsN):
                self.decisions[i] = uniform(self.bottom[i], self.top[i])
            if self.isValid():
                break
                
    def getObjectives(self):
        return [self.f1(self.decisions), self.f2(self.decisions)]
        
    def trim(self, x, d)  : # trim to legal range
        return max(self.low(d), min(x, self.high(d)))
        
    def getNumberOfDecisions(self):
        return 1
    
    
    
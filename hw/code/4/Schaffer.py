from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

import sys

class Schaffer:
    def __init__(self):
        self.top_bound = [10000]
        self.bottom_bound = [-10000]
        self.f1_low = 10**6
        self.f1_high = -(10**6)
        self.f2_low = 10**6
        self.f2_high = -(10**6)
        self.baseline_high = -(10**6)
        self.baseline_low = 10**6
        self.resetBaselines()
        self.threshold = self.baseline_low
    
    def decisions(self):
        return [0]
    
    def low(self, d):
        return self.bottom_bound[d]
    
    def high(self, d):
        return self.top_bound[d]
        
    def are_constraints_satisfied(self, x):
        return False if x[0] > 10**5 or x[0] < -10**5 else True
    
    def resetBaselines(self, rep = 1000000):
        f1low = f2low = sys.maxint
        f1high = f2high = -f1low
        low = sys.maxint
        high = -low
        for _ in xrange(0, rep):
            state = self.get_random_state()
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
        return x[0]**2
    
    def f2(self, x):
        return (x[0]-2)**2
        
    def energy(self, x):
        return self.f1(x) + self.f2(x)
    
    def aggregate_energy(self, x):
        return (sqrt(self.normalize_energy(self.f1(x), self.f1_low, self.f1_high)**2 + self.normalize_energy(self.f2(x), self.f2_low, self.f2_high)**2)/(sqrt(len(x))))
    
    def normalize_energy(self, energy, low, high):
        return (energy - low)/(high - low)
    
    def denormalize_energy(self, energy, low=None, high=None):
        low = low if low else self.baseline_low
        high = high if high else self.baseline_high
        
        return (high - low) * energy + low
    
    def get_random_state(self):
        while True:
            x = list()
            for low,high in zip(self.bottom_bound, self.top_bound):
                x.append(randint(low, high))
            # if self.are_constraints_satisfied(x):
            return x
                
    def trim(self, x, d)  : # trim to legal range
        return max(self.low(d), min(x, self.high(d)))
        
    def getNumberOfDecisions(self):
        return 1
    
    
    
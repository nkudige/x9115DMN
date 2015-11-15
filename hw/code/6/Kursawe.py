from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt
from math import sin

import sys

class Kursawe:
    def __init__(self):
        self.top_bound = [5, 5, 5]
        self.bottom_bound = [-5, -5, -5]
        self.f2_high = -10**6
        self.f2_low = 10**6
        self.f1_high = -10**6
        self.f1_low = 10**6
        self.baseline_high = -10**6
        self.baseline_low = 10**6
    
    def f1(self, ds):
        total = 0
        for i in range(len(ds)-1):
            e = -0.2 * sqrt(ds[i]**2 + ds[i+1]**2)
            total+= -10**(e)
        return total

    def f2(self, ds):
        total = 0
        for i in range(len(ds)):
            total+= abs(ds[i])**0.8 + 5*sin(ds[i]**3)
        return total
        
    def energy(self, x):
        return self.f1(x) + self.f2(x)
    
    def normalize_energy(self, e, low, high):
        return (e - low)/(high - low)
        
    def from_hell(self, x):
        return (sqrt(self.normalize_energy(self.f1(x), self.f1_low, self.f1_high)**2 + self.normalize_energy(self.f2(x), self.f2_low, self.f2_high)**2)/(sqrt(len(x))))
    
    def aggregate_energy(self, x):
        return 1 - self.from_hell(x) 
    
    def decisions(self):
        return [0, 1, 2]
        
    def low(self,index):
        return self.bottom_bound[index]
    
    def high(self, index):
        return self.top_bound[index]
        
    def are_constraints_satisfied(self, x):
        for i in x:
            if i > 5 or i < -5:
                return False
        return True
    
    def get_random_state(self):
        while True:
            x = list()
            for low,high in zip(self.bottom_bound, self.top_bound):
                x.append(low + random()*(high - low))
            if self.are_constraints_satisfied(x):
                return x
    
    def resetBaselines(self):
        f1low = f2low = sys.maxint
        f1high = f2high = -f1low
        for _ in range(0, 100000):
            state = self.get_random_state()
            f1_energy = self.f1(state)
            f2_energy = self.f2(state)
            if f1_energy > f1high:
                f1high = f1_energy
            if f1_energy < f1low:
                f1low = f1_energy
            if f2_energy < f2low:
                f2low = f2_energy
            if f2_energy > f2high:
                f2high = f2_energy
        self.f1_low = f1low
        self.f1_high = f1high
        self.f2_high = f2high
        self.f2_low = f2low
    
    def trim(self, x, d)  : # trim to legal range
        return max(self.low(d), min(x, self.high(d)))
    
    def getNumberOfDecisions(self):
        return 3
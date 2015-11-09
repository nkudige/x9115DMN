from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

import sys

class Schaffer:
    def __init__(self):
        self.top_bound = [10, 10, 5, 5, 6, 10]
        self.bottom_bound = [0, 0, 1, 1, 0, 0]
        self.f1_low = 10**6
        self.f1_high = -10**6
        self.f2_low = 10**6
        self.f2_high = -10**6
        self.baseline_high = -10**6
        self.baseline_low = 10**6
        self.threshold = -400
        self.resetBaselines()
        self.threshold = self.baseline_low
    
    def decisions(self):
        return [0, 1, 2, 3, 4, 5]
    
    def low(self, d):
        return self.bottom_bound[d]
    
    def high(self, d):
        return self.top_bound[d]
        
    def are_constraints_satisfied(self, x):
            if x[0] + x[1] - 2 < 0:
                    return False
            elif 6 - x[0] - x[1] < 0:
                    return False
            elif 2 - x[1] + x[0] < 0:
                    return False
            elif 2 - x[0] + 3*x[1] < 0:
                    return False
            elif 4 - x[3] - (x[2] -3)**2 < 0:
                    return False
            elif (x[4] -3)**3 + x[5] - 4 < 0:
                    return False
            elif self.energy(x) <= self.threshold:
                    return False
            else:
                    return True
    
    def resetBaselines(self):
        f1low = f2low = sys.maxint
        f1high = f2high = -f1low
        low = sys.maxint
        high = -low
        for _ in range(0, 1000):
            state = self.get_random_state()
            state_energy = self.energy(state)
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
            if state_energy > high:
                high = state_energy
            if state_energy < low:
                low = state_energy
                
        self.baseline_low = low
        self.baseline_high = high
        self.f1_low = f1high
        self.f1_low = f1low
        self.f2_high = f2high
        self.f2_low = f2low
    
    def f1(self, x):
        return -(25 * (x[0] - 2)**2 + (x[1] - 2)**2 + (x[2] - 1)**2 * (x[3] - 4)**2 + (x[4] - 1)**2)
    
    def f2(self, x):
        return sum([i**2 for i in x])
        
    def energy(self, x):
        return self.f1(x) + self.f2(x)
    
    def aggregate_energy(self, x):
        return (sqrt(self.normalize_energy(self.f1(x), self.f1_low, self.f1_high)**2 + self.normalize_energy(self.f2(x), self.f2_low, self.f2_high)**2)/(sqrt(len(x))))
    
    def normalize_energy(self, energy, low, high):
        return (energy - low)/(high - low)
    
    def get_random_state(self):
        while True:
            x = list()
            for low,high in zip(self.bottom_bound, self.top_bound):
                x.append(randrange(low, high))
            if self.are_constraints_satisfied(x):
                return x
    def trim(self, x, d)  : # trim to legal range
        return max(self.low(d), min(x, self.high(d)))
    
    
    
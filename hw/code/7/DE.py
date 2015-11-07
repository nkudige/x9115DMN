from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

import sys

class Thing():
    id = 0
    def __init__(self, **entries): 
        self.id = Thing.id = Thing.id + 1
        self.__dict__.update(entries)
    
    def __getitem__(self, key):
        return self.__dict__.get(key)
    

class DE():

    def __init__(self):
        self.top_bound = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        self.bottom_bound = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5]
        self.f2_high = -10**6
        self.f2_low = 10**6
        self.f1_high = -10**6
        self.f1_low = 10**6
    #Returns three different things that are not 'avoid'.
    def threeOthers(self, lst, avoid):
        def oneOther():
            x = self.a(lst)
            while x in seen: 
                x = self.a(lst)
            seen.append( x )
            return x
        # -----------------------
        seen = list(avoid.have)
        this = oneOther()
        that = oneOther()
        theOtherThing = oneOther()
        return this, that, theOtherThing

    def a(self, lst):
        return lst[self.n(len(lst))]

    def n(self, number):
        return int(uniform(0, number))
        
    def f1(self, x):
        return 0.7854 * x[0] * (x[1]**2) * (10*(x[2]**2)/3 + 14.933*x[2] - 43.0934) - \
        1.508 * x[0] * (x[5]**2 + x[6]**2) + \
        7.477 * (x[5]**3 + x[6]**3) + \
        0.7854 * (x[3]*(x[5]**2) + x[4]*(x[6]**2));

    def f2(self, x):
        return sqrt((745 * x[3] / (x[1]*x[2]))**2 + 1.69*10**7)/(0.1 * x[5]**3)
        
    def golinski_energy(self, x):
        return self.f1(x) + self.f2(x)
        
    def from_hell(self, x):
        return (sqrt(self.normalize_energy(self.f1(x), self.f1_low, self.f1_high)**2 + self.normalize_energy(self.f2(x), self.f2_low, self.f2_high)**2)/(sqrt(len(x))))
    
    def aggregate_energy(self, x):
        return 1 - self.from_hell(x) 
    
    def decisions(self):
        return [0, 1, 2, 3, 4, 5, 6]
    
    def low(self,index):
        return self.bottom_bound[index]
    
    def high(self, index):
        return self.top_bound[index]
    
    def trim(self, x, d)  : # trim to legal range
        return max(self.low(d), min(x, self.high(d)))
        
    def candidate(self):
        something = [uniform(self.low(d), self.high(d))
        for d in self.decisions()]
        new = Thing()
        new.have  = something
        new.score = self.golinski_energy(new.have)
        new.energy = self.aggregate_energy(new.have)
        return new
    
    def de(self, max     = 100,  # number of repeats 
            np      = 100,  # number of candidates
            f       = 0.75, # extrapolate amount
            cf      = 0.3,  # prob of cross-over 
            epsilon = 0.01
    ):
        frontier = [self.candidate() for _ in range(np)] 
        for k in range(max):
            total, n = self.update(f, cf, frontier)
            print "Frontier energy:" + str(total)
            if (n > 0 and total/n > (1 - epsilon)) or n <= 0:
                break
        return frontier

    def update(self, f, cf, frontier, total = 0.0, n = 0):
        for x in frontier:
            s = x.score
            new = self.extrapolate(frontier, x, f, cf)
            if new.score > s:
                x.energy = new.energy
                x.score = new.score
                x.have  = new.have
            n += 1
            total += x.energy
        return total,n
        
    def extrapolate(self, frontier, one, f, cf):
        out = Thing(id = one.id, have = list(one.have), score = self.golinski_energy(one.have), energy = self.aggregate_energy(one.have))
        two, three, four = self.threeOthers(frontier, one)
        changed = False
        for d in self.decisions():
            x, y, z = two.have[d], three.have[d], four.have[d]
            if random() < cf:
                changed = True
                new = x + f*(y - z)
                out.have[d]  = self.trim(new, d) # keep in range
        if not changed:
            d = self.a(self.decisions())
            out.have[d] = two.have[d]
        out.score = self.golinski_energy(out.have) # remember to score it
        out.energy = self.aggregate_energy(out.have)
        return out 
        
    def are_constraints_satisfied(self, x):
        status = True
        status = status and (1/(x[0]* x[1]**2 * x[2]) - 1/27 <= 0)
        status = status and (1/(x[0]* x[1]**2 * x[2]**2) - 1/397.5 <= 0)
        status = status and (x[3]**3/(x[1] * x[2]**2 * x[5]**4) - 1/1.93 <= 0)
        status = status and (x[4]**3/(x[1] * x[2] * x[6]**4) - 1/1.93 <= 0)
        status = status and (x[1]*x[2] - 40 <= 0)
        status = status and (x[0]/x[1] - 12 <= 0)
        status = status and (5 - x[0]/x[1] <= 0)
        status = status and (1.9 - x[3] +1.5*x[5] <= 0)
        status = status and (1.9 - x[4] +1.1*x[6] <= 0)
        status = status and (sqrt((745 * x[3] / (x[1]*x[2]))**2 + 1.69*10**7)/(0.1 * x[5]**3) <= 1300)
        a = 745*x[4]/(x[1]*x[2])
        b = 1.575 * 10**8
        status = status and ((a**2 + b)**0.5 / (0.1 * x[6]**3) <= 1100)
        return status

    def get_random_state(self):
        while True:
            x = list()
            for low,high in zip(self.bottom_bound, self.top_bound):
                x.append(low + random()*(high - low))
            if self.are_constraints_satisfied(x):
                return x

    def normalize_energy(self, e, low, high):
        return (e - low)/(high - low)

    def resetBaselines(self):
        f1low = f2low = sys.maxint
        f1high = f2high = -f1low
        for _ in range(0, 1000):
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

de = DE()
#print de.get_random_state()
de.resetBaselines()
print de.candidate().have
print de.candidate().score
de.de()

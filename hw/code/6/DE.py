from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt
#from models import Golinski
from Golinski import Golinski
from Schaffer import Schaffer

import sys

class Thing():
    id = 0
    def __init__(self, **entries): 
        self.id = Thing.id = Thing.id + 1
        self.__dict__.update(entries)
    
    def __getitem__(self, key):
        return self.__dict__.get(key)


class DE():
    def __init__(self, model = "Schaffer"):
        self.top_bound = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        self.bottom_bound = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5]
        self.f2_high = -10**6
        self.f2_low = 10**6
        self.f1_high = -10**6
        self.f1_low = 10**6
        self.evals = 0
        if model == "Schaffer":
            self.model = Schaffer()
        elif model == "Golinski":
            self.model = Golinski()
        self.best_solution = Thing()
        self.best_solution.score = 0;
        self.best_solution.energy = 1;
        
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

    def candidate(self):
        something = [uniform(self.model.low(d), self.model.high(d))
        for d in self.model.decisions()]
        new = Thing()
        new.have  = something
        new.score = self.model.energy(new.have)
        new.energy = self.model.aggregate_energy(new.have)
        return new
    
    def run(self, max     = 100,  # number of repeats 
            np      = 100,  # number of candidates
            f       = 0.75, # extrapolate amount
            cf      = 0.3,  # prob of cross-over 
            epsilon = 0.01,
            s       = 0.1
    ):
        frontier = [self.candidate() for _ in range(np)] 
        for k in range(max):
            total, n, output = self.update(f, cf, frontier)
            self.evals += n
            frontier.sort(key=lambda x: x.energy)
            #print output + "Frontier energy:" + str(total) + " Count:" + str(n) + " Max Energy:" + str(frontier[0].energy) + " Min Energy:" + str(frontier[len(frontier)-1].energy)
            min = frontier[0].energy
            max = frontier[len(frontier)-1].energy
            big = max - (max-min)*s/100
            new_frontier = [x for x in frontier if x.energy <= big]
            frontier = new_frontier
            if (n > 0 and total/n > (1 - epsilon)) or n <= 0 or len(frontier) < 3:
                break
        return self.best_solution.have

    def update(self, f, cf, frontier, total = 0.0, n = 0):
        output = ""
        for x in frontier:
            s = x.score
            new = self.extrapolate(frontier, x, f, cf)
            if s > new.score:
                output += "."
            elif new.score > s:
                x.energy = new.energy
                x.score = new.score
                x.have  = new.have
                output += "+"
            if new.score > self.best_solution.score:
                self.best_solution.score = new.score
                self.best_solution.have = new.have
                self.best_solution.energy = new.energy
                self.best_solution.evals = self.evals + n
                output += "!"
            if len(output) == 50:
                print output + " Best Solution: [",
                for a in self.best_solution.have:
                    print("%.2f " % a),
                print "] Energy: " + str(self.best_solution.energy) + " Evals: " + str(self.evals + n)
            n += 1
            total += x.energy
        return total, n, output
        
    def extrapolate(self, frontier, one, f, cf):
        out = Thing(id = one.id, have = list(one.have), score = self.model.energy(one.have), energy = self.model.aggregate_energy(one.have))
        two, three, four = self.threeOthers(frontier, one)
        changed = False
        for d in self.model.decisions():
            x, y, z = two.have[d], three.have[d], four.have[d]
            if random() < cf:
                changed = True
                new = x + f*(y - z)
                out.have[d]  = self.model.trim(new, d) # keep in range
        if not changed:
            d = self.a(self.model.decisions())
            out.have[d] = two.have[d]
        out.score = self.model.energy(out.have) # remember to score it
        out.energy = self.model.aggregate_energy(out.have)
        return out
    

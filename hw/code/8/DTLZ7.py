from __future__ import division

import random
import math
from a12 import a12


def loss(a, b, model):
    x, y = get_objectives(a, model), get_objectives(b, model)
    min_length = min(len(x), len(y))
    losses = [exp_loss(k, xi, yi, min_length) for k, (xi, yi) in enumerate(zip(x, y))]
    return sum(losses) / min_length
    
def exp_loss(k, x, y, n):
    return math.exp( (x-y) / n)
    
def get_objectives(state, model):
    return [objective(state) for objective in model.get_objectives()]

def is_continuously_dominated(one, two, model):
    return loss(one, two, model) < loss(two, one, model)

class DTLZ7():

    def __init__(self, decisions, objectives):
        #BaseModel.__init__(self)
        self.model_name = "DTLZ7"
        self.low = 10**5
        self.high = -10**5
        self.number_vars = decisions
        self.number_objectives = objectives
        self.top_bound = [1.0]*decisions
        self.bottom_bound = [0.0]*decisions
        self.resetBaselines()
        
    def get_random_state(self):
        random_state = list()
        while True:
            for i, j in zip(self.bottom_bound, self.top_bound):
                if isinstance(i, int) and isinstance(j, int):
                    random_state.append(random.randrange(i, j))
                else:
                    random_state.append(random.uniform(i, j))
            return random_state
        
    def type1(self, state1, state2):
        return is_continuously_dominated(state1, state2, self)
        
    def resetBaselines(self):
        self.low = 10**5
        self.high = -10**5
        for _ in xrange(0, 10000):
            soln = self.get_random_state()
            energy = self.energy(soln)

            if energy > self.high:
                self.high = energy

            if energy < self.low:
                self.low = energy

    def energy(self, x):
        energy = 0
        for obj in self.get_objectives():
            energy += obj(x)
        return energy

    def normalize_energy(self, energy):
        return (energy - self.low)/(self.high - self.low)
    
    def lessThan(self, x, y):
        return x < y
        
    def g(self, x):
        y = 0.0
        for i in xrange(0, self.number_vars):
            y += x[i]
        return(9*y/self.number_vars)

    def h(self, f, g, x):
        y = 0.0
        for i in xrange(0, self.number_objectives - 1):
            y += (f[i](x) / (1 + g)) * (1 + math.sin(3 * math.pi * f[i](x)))
        return self.number_objectives - y

    def last_obj(self, x, f):
        g = 1 + self.g(x)
        res = (1 + g) * self.h(f, g, x)
        return res

    def obj(self, x, i):
        return x[i]

    def get_objectives(self):
        f = [None] * self.number_objectives
        for i in xrange(0, self.number_objectives - 1):
            f[i] = lambda x : self.obj(x,i)
        f[self.number_objectives - 1] = lambda x : self.last_obj(x, f)
        return f
        
    def getNumberOfDecisions(self):
        return self.number_vars
    
    def type2(self, era_one, era_two):
        for objective in self.get_objectives():
            era_one_objective = []
            era_two_objective = []
            for i in xrange(0, len(era_one)):
                era_one_objective.append(objective(era_one[i]))
                era_two_objective.append(objective(era_two[i]))
            if (a12(era_one_objective, era_two_objective) > 0.56):
                return 5
        return -1
        
    def decisions(self):
        return [i for i in xrange(0, self.number_vars-1)]

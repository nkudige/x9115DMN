from __future__ import division
from random import randrange
from random import randint
from random import random

import sys

class osyzka:
        def get_random_state(self):
                while True:
                        x = list()
                        for low,high in zip(self.bottom_bound, self.top_bound):
                                x.append(randrange(low, high))
                        if self.are_constraints_satisfied(x):
                                return x

        def __init__(self, probability = 0.5, no_steps = 10, baseline_top = -10**6, baseline_bottom = 10**6):
                self.n = 6
                self.p = probability
                self.evals = 0
                self.top_bound = [10, 10, 5, 10, 7, 10]
                self.bottom_bound = [0, 1, 1, 0, 0, 3]
                self.steps = no_steps
                self.number_of_evaluations = 0
                self.threshold = - 400
                self.baseline_high = baseline_top
                self.baseline_low = baseline_bottom
                self.current_state = self.get_random_state()
                self.resetBaselines()
                #print "baseline high:" + str(self.baseline_high)
                self.threshold = self.baseline_low

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
                elif self.osyczka_energy(x) <= self.threshold:
                        return False
                else:
                        return True

        def resetBaselines(self):
                low = sys.maxint
                high = -low
                for _ in range(0, 1000):
                        state = self.get_random_state()
                        state_energy = self.osyczka_energy(state)
                        if state_energy > high:
                                high = state_energy
                        if state_energy < low:
                                low = state_energy
                self.baseline_low = low
                self.baseline_high = high

        def osyczka_energy(self, x):
                f1 = -(25 * (x[0] - 2)**2 + (x[1] - 2)**2 + (x[2] - 1)**2 * (x[3] - 4)**2 + (x[4] - 1)**2)
                f2 = sum([i**2 for i in x])
                return f1 + f2

        def normalize_energy(self, energy):
                return (energy - self.baseline_low)/(self.baseline_high - self.baseline_low)

        def modify_to_better_state(self, state, index):
                if(index > len(self.top_bound)):
                        return None
                increment = (self.top_bound[index] - self.bottom_bound[index])/self.steps
                temp_state = list(state)
                best_state = state
                for _ in range(0, self.steps):
                        temp_state[index] += increment
                        self.evals += 1
                        if self.osyczka_energy(temp_state) < self.osyczka_energy(best_state) and self.are_constraints_satisfied(temp_state):
                                best_state = list(temp_state)
                state = best_state
                return state

        def retry(self, state):
                index = randint(0, 5)
                temp_state = list(state)
                if self.p < random():
                        temp_state[index] = randrange(self.bottom_bound[index], self.top_bound[index])
                        if self.are_constraints_satisfied(temp_state):
                                return temp_state, "?"
                        else:
                                return state,"."
                else:
                        temp_state = self.modify_to_better_state(temp_state, index)
                        if temp_state == state:
                                return temp_state, "."
                        else:
                                return temp_state, "+"

        def max_walk_sat(self):
                max_tries = 100
                max_changes = 50
                p = 0.5
                self.resetBaselines()
                print self.baseline_high
                print self.baseline_low
                number_of_evaluations = 0
                best_state = self.get_random_state()
                for _ in range(0, max_tries):
                        current_state = self.get_random_state()
                        output = str()
                        for i in range(0, max_changes):
                                if self.osyczka_energy(current_state) < self.threshold:
                                        return current_state
                                else:
                                        new_state, operation = self.retry(current_state)
                                output += operation
                                if(self.osyczka_energy(current_state) < self.osyczka_energy(best_state)):
                                        best_state = current_state
                                if(self.osyczka_energy(new_state) < self.osyczka_energy(best_state)):
                                        best_state = new_state
                        print output + "current best state energy(normalized) = " + str(self.normalize_energy(self.osyczka_energy(best_state))) + " Evaluations: " + str(self.evals)
                return best_state

model = osyzka()
model.max_walk_sat()
print "Total evaluations: " + str(model.evals)

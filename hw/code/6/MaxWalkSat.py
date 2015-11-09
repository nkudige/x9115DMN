from __future__ import division
from random import randrange
from random import randint
from random import random
#from models import Schaffer
from Schaffer import Schaffer
from Golinski import Golinski

import sys

class MaxWalkSat:
        def __init__(self, model = "Schaffer", probability = 0.5, no_steps = 10, baseline_top = -10**6, baseline_bottom = 10**6):
                self.n = 6
                self.p = probability
                self.evals = 0
                self.steps = no_steps
                self.number_of_evaluations = 0
                self.threshold = - 400
                if model == "Schaffer":
                        self.model = Schaffer()
                elif model == "Golinski":
                        self.model = Golinski()
                self.model.resetBaselines()
                self.current_state = self.model.get_random_state()

        def modify_to_better_state(self, state, index):
                if(index > len(self.model.top_bound)):
                        return None
                increment = (self.model.top_bound[index] - self.model.bottom_bound[index])/self.steps
                temp_state = list(state)
                best_state = state
                for _ in range(0, self.steps):
                        temp_state[index] += increment
                        self.evals += 1
                        if self.model.energy(temp_state) < self.model.energy(best_state) and self.model.are_constraints_satisfied(temp_state):
                                best_state = list(temp_state)
                state = best_state
                return state

        def retry(self, state):
                index = randint(0, 5)
                temp_state = list(state)
                if self.p < random():
                        #print self.model.bottom_bound[index]
                        #print self.model.top_bound[index]
                        temp_state[index] = self.model.bottom_bound[index] + (self.model.top_bound[index] - self.model.bottom_bound[index])*random()
                        if self.model.are_constraints_satisfied(temp_state):
                                return temp_state, "!"
                        else:
                                return state,"."
                else:
                        temp_state = self.modify_to_better_state(temp_state, index)
                        if temp_state == state:
                                return temp_state, "."
                        else:
                                return temp_state, "+"

        def run(self):
                max_tries = 100
                max_changes = 50
                self.model.resetBaselines()
                best_state = self.model.get_random_state()
                for _ in range(0, max_tries):
                        current_state = self.model.get_random_state()
                        output = str()
                        for i in range(0, max_changes):
                                if self.model.energy(current_state) < self.threshold:
                                        return current_state
                                else:
                                        new_state, operation = self.retry(current_state)
                                output += operation
                                if(self.model.energy(current_state) < self.model.energy(best_state)):
                                        best_state = current_state
                                if(self.model.energy(new_state) < self.model.energy(best_state)):
                                        best_state = new_state
                        print output + "current best state energy(normalized) = " + str(self.model.aggregate_energy(best_state)) + " Evaluations: " + str(self.evals)
                return best_state



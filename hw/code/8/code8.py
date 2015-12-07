from __future__ import division
import sys, random, math, time
from random import randrange
from random import randint
from random import random
from random import uniform
from Schaffer import Schaffer
from Osyczka import Osyczka
from Golinski import Golinski
from Kursawe import Kursawe
from a12 import a12
from sk import rdivDemo
from DTLZ7 import DTLZ7
import math
import sys


class SA:
  def __init__(self, model = "Schaffer"):
    self.evals = 0
    if model == "Schaffer":
      self.model = Schaffer()
    elif model == "Osyczka":
      self.model = Osyczka()
    elif model == "Golinski":
      self.model = Golinski()
    elif model == "Kursawe":
      self.model = Kursawe()
    elif model == "DTLZ7":
      self.model = DTLZ7(10, 2)

  def __repr__(self):
    return time.strftime("%Y-%m-%d %H:%M:%S") + "\nSimulated Annealing on the Schaffer model\n"
  
  def P(self, old_e, new_e, k):
    return math.e ** ((old_e - new_e) / k)

  def run(self):
    kmax = 1000
    max_e = -0.1
    output = ''
    
    current_s = self.model.get_random_state()
    best_s = current_s
    
    current_e = self.model.normalize_energy(self.model.energy(current_s))
    best_e = current_e
    MAX_LIVES = 10
    ERA_LENGTH = 100
    k = 1
    era_List = []
    current_era = []
    lives = MAX_LIVES
    while k < kmax and current_e > max_e:
      neighbor_s = self.model.get_random_state()
      # print 'Neighbor: ' + str(neighbor_s)
      
      neighbor_e = self.model.normalize_energy(self.model.energy(neighbor_s))
      # print current_e, neighbor_e, tmp
      if self.model.type1(best_s, neighbor_s):
        # print "Neighbor better " + str(best_e) + " " + str(neighbor_e)
        best_s, best_e = neighbor_s, neighbor_e
        temp = ' !'
      
      if self.model.type1(neighbor_s, current_s):
        current_s, current_e = neighbor_s, neighbor_e
        temp = ' +'
        
      elif self.P(current_e, neighbor_e, (1-(float(k)/kmax))**5) > random():
        current_s, current_e = neighbor_s, neighbor_e
        temp = ' ?'
        
      else:
        temp = ' .'
      
      if temp != ' .':
        current_era.append(neighbor_s)
        if len(current_era) == ERA_LENGTH:
          #print current_era
          if len(era_List) > 0:
            increment = self.model.type2(current_era, era_List[-1])
            lives += increment
            if increment <= 0:
                    print "Reducing lives by 1"
            if lives <= 0:
                print "Early termination"
                return best_e
          era_List.append(current_era)
          current_era = []
      
      output += temp
      if k % 25 == 0:
        print output + "Best state: ", best_e
        output = ''
    
      k += 1

    print 'Best State Found: ' + str(best_s)
    print 'Energy At Best State: ' + str(best_e)
    
    return best_e


print "DTLZ7"
sa = SA(model = "DTLZ7")
sa.run()


class MaxWalkSat:
        def __init__(self, model = "Kursawe", probability = 0.5, no_steps = 20, baseline_top = -10**6, baseline_bottom = 10**6):
                self.n = 6
                self.p = probability
                self.evals = 0
                self.steps = no_steps
                self.number_of_evaluations = 0
                self.threshold = - 400
                if model == "Osyczka":
                        self.model = Osyczka()
                elif model == "Golinski":
                        self.model = Golinski()
                elif model == "Kursawe":
                        self.model = Kursawe()
                elif model == "Schaffer":
                        self.model = Schaffer()
                elif model == "DTLZ7":
                        self.model = DTLZ7(10, 2)
                self.model.resetBaselines()
                #self.threshold = self.model.baseline_low
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
                        if self.model.energy(temp_state) < self.model.energy(best_state): #and self.model.are_constraints_satisfied(temp_state):
                                best_state = list(temp_state)
                state = best_state
                return state

        def retry(self, state):
                index = randint(0, (self.model.getNumberOfDecisions() - 1))
                temp_state = list(state)
                if self.p < random():
                        temp_state[index] = self.model.bottom_bound[index] + (self.model.top_bound[index] - self.model.bottom_bound[index])*random()
                        # if self.model.are_constraints_satisfied(temp_state):
                        #         return temp_state
                        # else:
                        #         return state
                else:
                        temp_state = self.modify_to_better_state(temp_state, index)
                        if temp_state == state:
                                return temp_state
                        else:
                                return temp_state

        def run(self):
                max_tries = 100
                max_changes = 100
                self.model.resetBaselines()
                best_state = self.model.get_random_state()
                output = str()
                MAX_LIVES = 10
                ERA_LENGTH = 10
                era_List = []
                current_era = []
                lives = MAX_LIVES
                for _ in range(0, max_tries):
                        current_state = self.model.get_random_state()
                        for i in range(0, max_changes):
                                if self.model.energy(current_state) < self.threshold:
                                        return current_state
                                else:
                                        new_state = self.retry(current_state)
                                operation = ""
                                while new_state == None:
                                        new_state = self.retry(current_state)
                                if self.model.type1(best_state, new_state):
                                        best_state = new_state
                                        operation = "!"
                                elif self.model.type1(current_state, new_state):
                                        operation = "+"        
                                elif self.model.type1(new_state, current_state):
                                        operation = "."
                                current_era.append(new_state)
                                if len(current_era) == ERA_LENGTH and len(era_List) > 0:
                                        lives += self.model.type2(current_era, era_List[-1])
                                        if lives <= 0:
                                                print "Early termination"
                                                break
                                        era_List.append(current_era)
                                        current_era = []
                                output += operation
                                if len(output) == 50:
                                        output + " current best state energy = " + str(best_state) + " Evaluations: " + str(self.evals)
                                        output = ""
                print  output + " current best state energy = " + str(best_state) + " Evaluations: " + str(self.evals)
                return best_state


print "DTLZ7"
MWS = MaxWalkSat("DTLZ7")
MWS.run()





class Thing():
    id = 0
    def __init__(self, **entries): 
        self.id = Thing.id = Thing.id + 1
        self.__dict__.update(entries)
    
    def __getitem__(self, key):
        return self.__dict__.get(key)


class DE():
    def __init__(self, model = "DTLZ7"):
        self.top_bound = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        self.bottom_bound = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5]
        self.f2_high = -10**6
        self.f2_low = 10**6
        self.f1_high = -10**6
        self.f1_low = 10**6
        self.evals = 0
        self.median = []
        if model == "Osyczka":
            self.model = Osyczka()
        elif model == "Golinski":
            self.model = Golinski()
        elif model == "Kursawe":
            self.model = Kursawe()
        elif model == "Schaffer":
            self.model = Schaffer()
        elif model == "DTLZ7":
            self.model = DTLZ7(10, 2)
        self.best_solution = Thing()
        self.best_solution.score = 0;
        self.best_solution.energy = 1;
        self.best_solution.have = []
        self.previous_era = []
        
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
        # something = [uniform(self.model.low(d), self.model.high(d))
        # for d in self.model.decisions()]
        something = self.model.get_random_state()
        new = Thing()
        new.have  = something
        new.score = self.model.energy(new.have)
        new.energy = self.model.energy(new.have)
        return new
    
    def run(self, maximum = 100,  # number of repeats 
            np      = 100,  # number of candidates
            f       = 0.75, # extrapolate amount
            cf      = 0.3,  # prob of cross-over 
            epsilon = 0.01,
            s       = 0.1
    ):
        print "asd" + str(np)
        frontier = [self.candidate() for _ in range(np)] 
        print "test"
        median = []
        print maximum
        for k in range(0, 100):
            total, n, output = self.update(f, cf, frontier)
            self.evals += n
            frontier.sort(key=lambda x: x.energy)
            #print output + "Frontier energy:" + str(total) + " Count:" + str(n) + " Max Energy:" + str(frontier[0].energy) + " Min Energy:" + str(frontier[len(frontier)-1].energy)
            min = frontier[0].energy
            max = frontier[len(frontier)-1].energy
            median.append(frontier[int(len(frontier)/2)].score)
            big = max - (max-min)*s/100
            new_frontier = [x for x in frontier if x.energy <= big]
            frontier = new_frontier
            if (n > 0 and total/n > (1 - epsilon)) or n <= 0 or len(frontier) < 3:
                break
        print "Median values:"
        print median
        return self.previous_era

    def update(self, f, cf, frontier, total = 0.0, n = 0):
        output = ""
        MAX_LIVES = 10
        ERA_LENGTH = 10
        era_List = []
        current_era = []
        lives = MAX_LIVES
        for x in frontier:
            s = x.energy
            new = self.extrapolate(frontier, x, f, cf)
        #     if self.model.type1(x.have, new.have):
        #         output += "."
            if s < new.energy:
                output += "."
        #     elif self.model.type1(new.have, x.have):
        #         x.energy = new.energy
        #         x.score = new.score
        #         x.have  = new.have
        #         output += "+"
            elif new.energy < s:
                x.energy = new.energy
                x.score = new.score
                x.have  = new.have
                output += "+"
        #     if self.model.type1(new.have, self.best_solution.have):
        #         self.best_solution.score = new.score
        #         self.best_solution.have = new.have
        #         self.best_solution.energy = new.energy
        #         self.best_solution.evals = self.evals + n
        #         output += "!"    
            if new.energy < self.best_solution.energy:
                self.best_solution.score = new.score
                self.best_solution.have = new.have
                self.best_solution.energy = new.energy
                self.best_solution.evals = self.evals + n
                output += "!"
            if len(output) == 50:
                print output + " Best Solution: [",
                for a in self.best_solution.have:
                    print("%.2f " % a),
                print "] Energy: " + str(self.best_solution.score) + " Evals: " + str(self.evals + n)
            current_era.append(x.have)
            if len(current_era) == ERA_LENGTH and len(era_List) > 0:
                increment = self.model.type2(current_era, era_List[-1])
                lives += increment
                if lives <= 0:
                    self.previous_era = era_List[-1]
                    print "Early termination"
                    break
                era_List.append(current_era)
                current_era = []
            n += 1
            total += x.energy
        return total, n, output
        
    def extrapolate(self, frontier, one, f, cf):
        out = Thing(id = one.id, have = list(one.have), score = self.model.energy(one.have), energy = self.model.energy(one.have))
        two, three, four = self.threeOthers(frontier, one)
        changed = False
        for d in self.model.decisions():
            x, y, z = two.have[d], three.have[d], four.have[d]
            if random() < cf:
                changed = True
                new = x + f*(y - z)
                out.have[d]  = max(0.0, min(new, 1.0)) # keep in range
        if not changed:
            d = self.a(self.model.decisions())
            out.have[d] = two.have[d]
        out.score = self.model.energy(out.have) # remember to score it
        out.energy = self.model.energy(out.have)
        return out
        


model = DTLZ7(10, 2)
eras=[]
for i in xrange(20):
    for algorithm in ["MaxWalkSat", "SA", "DE"]:
        if algorithm == "MaxWalkSat":
            algo = MaxWalkSat("DTLZ7")
        elif algorithm == "SA":
            algo = SA("DTLZ7")
        elif algorithm == "DE":
            algo = DE("DTLZ7")
        era = [model.normalize_val(model.eneergy(val)) for val in algo.run()]
        era.insert(0, algorithm + str(i))
        eras.append(era)
        print era

print rdivDemo(eras)
            
        

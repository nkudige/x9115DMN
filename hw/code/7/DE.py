from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

import sys

class DE:

    def __init__(self):
        self.top_bound = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        self.bottom_bound = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5]
        self.baseline_high = -10**6
        self.baseline_low = 10**6
        
    #Returns three different things that are not 'avoid'.
    def threeOthers(self, lst, avoid):
      def oneOther():
          x = a(lst)
          while x in seen: 
              x = a(lst)
          seen.append( x )
          return x
  # -----------------------
      seen = list(avoid)
      this = oneOther()
      that = oneOther()
      theOtherThing = oneOther()
      return this, that, theOtherThing


    def a(self, lst):
        return lst[n(len(lst))]

    def n(self, number):
        return int(uniform(0,number))

    def golinski_energy(self, x):
        self.f1 = 0.7854 * x[0] * (x[1]**2) * (10*(x[2]**2)/3 + 14.933*x[2] - 43.0934) - \
        1.508 * x[0] * (x[5]**2 + x[6]**2) + \
        7.477 * (x[5]**3 + x[6]**3) + \
        0.7854 * (x[3]*(x[5]**2) + x[4]*(x[6]**2))
        f2 = sqrt((745 * x[3] / (x[1]*x[2]))**2 + 1.69*10**7)/(0.1 * x[5]**3)
        return f1 + f2

    def are_constraints_satisfied(self, x):
        #print x
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
            #print self.are_constraints_satisfied(x)
            if self.are_constraints_satisfied(x):
                return x

    def normalize_energy(self, e):
        return (e - self.baseline_low)/(self.baseline_high - self.baseline_low)

    def resetBaselines(self):
        low = sys.maxint
        high = -low
        for _ in range(0, 1000):
            state = self.get_random_state()
            state_energy = self.golinski_energy(state)
            if state_energy > high:
                high = state_energy
            if state_energy < low:
                low = state_energy
        self.baseline_low = low
        self.baseline_high = high

de = DE()
print de.get_random_state()


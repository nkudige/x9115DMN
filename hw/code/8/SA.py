import sys, random, math, time

from Schaffer import Schaffer
from Osyczka import Osyczka
from Golinski import Golinski
from Kursawe import Kursawe
from a12 import a12

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
    
    current_e = self.model.normalize_energy(self.model.energy(current_s), self.model.baseline_low, self.model.baseline_high)
    best_e = current_e
    
    k = 1
    current_era = []
    eras = []
    lives = 5
    ERA_LENGTH = 10
    while k < kmax and current_e > max_e:
      neighbor_s = self.model.get_random_state()
      # print 'Neighbor: ' + str(neighbor_s)
      neighbor_e = self.model.normalize_energy(self.model.energy(neighbor_s), self.model.baseline_low, self.model.baseline_high)
      # print current_e, neighbor_e, tmp
      
      if neighbor_e < best_e:
        best_s, best_e = neighbor_s, neighbor_e
        output += ' !'
      
      if neighbor_e < current_e:
        current_s, current_e = neighbor_s, neighbor_e
        output += ' +'
        
      elif self.P(current_e, neighbor_e, (1-(float(k)/kmax))**5) > random.random():
        current_s, current_e = neighbor_s, neighbor_e
        output += ' ?'
        
      else:
        output += ' .'
      
      current_era.append(self.model.normalize_energy(current_e, self.model.baseline_low, self.model.baseline_high))
      if len(current_era) == ERA_LENGTH and len(eras) > 0:
        if a12(current_era, eras[-1]) < 0.56:
          lives -= 1
          print "Lives:" + str(lives) + " a12 statistic:" + str(a12(current_era, eras[-1])),
        else:
          lives = 5
      if len(current_era) == ERA_LENGTH:
        eras.append(current_era)
        current_era = []
        if lives <= 0:
          print "Early termination"
          break
      if k % 25 == 0:
        print ', %4d, : %d, %25s' % (k, self.model.denormalize_energy(best_e), output)
        output = ''
    
      k += 1
      
    print
    print 'Best State Found: ' + str(best_s)
    print 'Energy At Best State: ' + str(self.model.denormalize_energy(best_e))
    print
    
    return best_e

if __name__ == '__main__':
  sa = SA("Schaffer")
  sa.run()
import sys, random, math, time

from Schaffer import Schaffer

class SA:
  def __init__(self, model = "Schaffer"):
    if model == "Schaffer":
      self.model = Schaffer()

  def __repr__(self):
    return time.strftime("%Y-%m-%d %H:%M:%S") + "\nSimulated Annealing on the Schaffer model\n"
  
  def P(self, old_e, new_e, k):
    return math.e ** ((old_e - new_e) / k)

  def run(self):
    print self
    kmax = 1000
    max_e = -0.1
    output = ''
    
    current_s = self.model.get_random_state()
    best_s = current_s
    
    current_e = self.model.normalize_energy(self.model.energy(current_s))
    best_e = current_e
    
    k = 1
    
    while k < kmax and current_e > max_e:
      neighbor_s = self.model.get_random_state()
      # print 'Neighbor: ' + str(neighbor_s)
      neighbor_e = self.model.normalize_energy(self.model.energy(neighbor_s))
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
  sa = SA()
  sa.run()
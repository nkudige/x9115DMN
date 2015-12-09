from __future__ import division
from random import seed, randint, uniform
import numpy as np, pandas as pd
from DTLZ import *
from Schaffer import *

sd = 0

class GA():
    def __init__(self):
        self.top_bound = [1.0, 1.0, 500, 5000, 1000]
        self.bottom_bound = [0.0, 0.0, 1, 1, 1]

    def decisions(self):
        # mutation, crossover, candidates, generations, early termination threshold
        return [0, 1, 2, 3, 4]

    def low(self, d):
        return self.bottom_bound[d]
    
    def high(self, d):
        return self.top_bound[d]

    def energy(self, x):
        return runner(*x)
    
    def aggregate_energy(self, x):
        return energy(x)
    
    def normalize_energy(self, energy, low, high):
        return (energy - low)/(high - low)
    
    def denormalize_energy(self, energy, low=None, high=None):
        low = low if low else self.baseline_low
        high = high if high else self.baseline_high
        return (high - low) * energy + low
        
mxsz = 0

def is_binarydominant(x, y):
    x = x.getObjectives() if not isinstance(x, list) else x
    y = y.getObjectives() if not isinstance(y, list) else y

    if x == y:
        return False

    for (objective_x, objective_y) in zip(x, y):
        if objective_x > objective_y:
            return False

    return True

def mutate(mutation_rate, candidate):
    while True:
        for i in xrange(candidate.decisionsN):
            if random() < mutation_rate:
                candidate.decisions[i] = uniform(candidate.bottom[i], candidate.top[i])
        if candidate.isValid():
            break

    return candidate

def crossover(daddy, mummy, baby, point=None):
    while True:
        crossover_point = randint(0, len(daddy.decisions) - 1) if not point else point
        baby.decisions = daddy.decisions[:crossover_point] + mummy.decisions[crossover_point:]
        if baby.isValid():
            break

    return baby

def fight(best_frontier, new_frontier):
    better = []

    for i, c1 in enumerate(new_frontier):
        for j, c2 in enumerate(best_frontier):
            if is_binarydominant(c1, c2):
                better.append(c1)
                best_frontier.remove(c2)

    if better:
        best_frontier.extend(better)
        return (best_frontier, False)
    
    return (best_frontier, True)

def baselines(Model, decisionsN, objectivesN, reps):
    population = [Model(decisionsN, objectivesN) for _ in xrange(reps)]
    print [c.getObjectives() for c in population if len(c.getObjectives()) < 2]
    mx = [np.max([c.getObjectives()[i] for c in population]) for i in xrange(objectivesN)]
    mn = [np.min([c.getObjectives()[i] for c in population]) for i in xrange(objectivesN)]
    return mn, mx

def gen_candidate(Model, decisionsN, objectivesN):
    return Model(decisionsN,objectivesN)

def get_pareto_frontier(population):
    i, frontier = 0, []
    for candidate in population:
        for another_candidate in population:
            if is_binarydominant(another_candidate, candidate):
                break
        else:
            frontier.append(candidate)
            i += 1
            if i == 50:
                break

    return frontier

def terminate_early(last, now, threshold):
    changed = len(set(now) - set(last))
    return True if 1.0 * changed / len(last) <= threshold else False

def GeneticAlgorithms(Model, decisionsN, objectivesN, sd, candidatesN, generations, mutation_rate, inactivity_max, threshold=0.1, crossover_point=None):
    global mxsz
    seed(sd)

    population = [gen_candidate(Model, decisionsN, objectivesN) for _ in xrange(candidatesN)]
    pareto_frontier = get_pareto_frontier(population)
    best_frontier = pareto_frontier[:]
    best_candidate_energy = 0
    last_100_best_frontier = best_frontier[:]
    
    for i in xrange(1, generations + 1):
        if i % inactivity_max == 0:
            if terminate_early(last_100_best_frontier, best_frontier, threshold):
                print 'Rep:', sd, '   Terminated at Gen:', i, '    Best Energy:', best_candidate_energy
                break
            last_100_best_frontier = best_frontier[:]

        next_generation = []
        for j in xrange(candidatesN):
            baby = Model()
            (daddy, mummy) = np.random.choice(len(pareto_frontier), 2, replace=True)
            baby = crossover(pareto_frontier[daddy],pareto_frontier[mummy], baby, crossover_point)
            baby = mutate(mutation_rate, baby)
            baby_energy = baby.eval()
            best_candidate_energy = baby_energy if baby_energy > best_candidate_energy else best_candidate_energy
            next_generation.append(baby)

        pareto_frontier_new = get_pareto_frontier(next_generation)
        (best_frontier, no_change) = fight(best_frontier, pareto_frontier_new)

        population = next_generation
        pareto_frontier = pareto_frontier_new

    return best_frontier

def is_in_hypervolume(pebble, pareto_frontier):
    for candidate in pareto_frontier:
        if is_binarydominant(candidate, pebble):
            return True
    return False

def hveval(frontier, mn, mx, samples):
    count, m = 0, frontier[0].objectivesN

    for i in xrange(samples):
        pebble = [uniform(mn[k],mx[k]) for k in xrange(m)]
        if is_in_hypervolume(pebble, frontier):
            count = count + 1

    return 1.0 * count / samples

def interquartilerange(a):
  q25, q75 = np.percentile(a, [25 ,75])
  return q75 - q25

def analyze_results(hypervolume, models, model_names, objectives, decisins):
    y = {}
    m = [model_names[x] for x in models]

    for model in m:
        y[model] = {}
        a=[]
        for objectivesN in objectives:
            y[model][objectivesN] = {}
            b=[]
            for decisionsN in decisins:
                y[model][objectivesN][decisionsN] = []
                y[model][objectivesN][decisionsN].append(np.mean(hypervolume[model][objectivesN][decisionsN]))
                y[model][objectivesN][decisionsN].append(np.median(hypervolume[model][objectivesN][decisionsN]))
                y[model][objectivesN][decisionsN].append(interquartilerange(hypervolume[model][objectivesN][decisionsN]))
                b.append(str(np.mean(hypervolume[model][objectivesN][decisionsN])) + ', ' + str(np.median(hypervolume[model][objectivesN][decisionsN])) + ', ' + str(interquartilerange(hypervolume[model][objectivesN][decisionsN])))
            a.append(b)

        print 'Model: ', model
        print pd.DataFrame(data = a, columns = decisins, index = objectives)

def runner(mutation_rate, crossover_point, candidates, generations, terminate_early):
    global sd

    model =Schaffer
    decisionsN = 1
    objectivesN = 2

    pareto_frontier = GeneticAlgorithms(model, decisionsN, objectivesN, sd, candidates, generations, mutation_rate, terminate_early, 0, crossover_point)
    sd += 1

if __name__ == '__main__':
    candidatesN = 100
    generations = 1000
    mutation_rate = 0.00001
    inactivity_max = 100
    threshold = 0

    models = [DTLZ1, DTLZ3, DTLZ5, DTLZ7]
    objectives = [2, 4, 6, 8]
    decisins = [10, 20, 40]
    model_names = {DTLZ1: 'DTLZ1', DTLZ3: 'DTLZ3', DTLZ5: 'DTLZ5', DTLZ7: 'DTLZ7'}
    
    models = [Schaffer]
    objectives = [2]
    decisins = [1]
    model_names = {Schaffer: 'Schaffer'}
    
    hypervolume = {}

    for model in models:
        hypervolume[model_names[model]] = {}
        for objectivesN in objectives:
            hypervolume[model_names[model]][objectivesN] = {}
            for decisionsN in decisins:
                print 'Model: ', model, ' Objectives: ', objectivesN, ' Decisions: ', decisionsN
                hypervolume[model_names[model]][objectivesN][decisionsN] = []
                (mn, mx) = baselines(model, decisionsN, objectivesN, 10)
                for sd in xrange(1):
                    pareto_frontier = GeneticAlgorithms(model, decisionsN, objectivesN, sd, candidatesN, generations, mutation_rate, inactivity_max, threshold)
                    hypervolume[model_names[model]][objectivesN][decisionsN].append(hveval(pareto_frontier, mn, mx, 10))

    analyze_results(hypervolume, models, model_names, objectives, decisins)
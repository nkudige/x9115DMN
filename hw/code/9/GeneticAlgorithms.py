from __future__ import division
import random, pickle
import numpy as np
import pandas as pd
from analysis import *
from DTLZ import *

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
            if random.random() < mutation_rate:
                candidate.decisions[i] = random.uniform(candidate.bottom[i], candidate.top[i])
        if candidate.isValid():
            break

    return candidate

def crossover(daddy, mummy, baby):
    while True:
        crossover_point = random.randint(0, len(daddy.decisions) - 1)
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

def GeneticAlgorithms(Model, decisionsN, objectivesN, sd, candidatesN, generations, mutation_rate, inactivity_max, threshold=0.1):
    global mxsz
    random.seed(sd)

    population = [gen_candidate(Model, decisionsN, objectivesN) for _ in xrange(candidatesN)]
    pareto_frontier = get_pareto_frontier(population)
    best_frontier = pareto_frontier[:]
    best_candidate_energy = 0
    last_100_best_frontier = best_frontier[:]
    
    # inactivity_current = 0
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
            baby = crossover(pareto_frontier[daddy],pareto_frontier[mummy], baby)
            baby = mutate(mutation_rate, baby)
            baby_energy = baby.eval()
            best_candidate_energy = baby_energy if baby_energy > best_candidate_energy else best_candidate_energy
            next_generation.append(baby)

        pareto_frontier_new = get_pareto_frontier(next_generation)
        (new_best_frontier, no_change) = fight(best_frontier, pareto_frontier_new)

        # if no_change:
        #     inactivity_current += 1
        #     if inactivity_current == inactivity_max:
        #         break
        # else:
        #     best_frontier = new_best_frontier
        best_frontier = new_best_frontier

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
        pebble = [random.uniform(mn[k],mx[k]) for k in xrange(m)]
        if is_in_hypervolume(pebble, frontier):
            count = count + 1

    return 1.0 * count / samples

if __name__ == '__main__':
    candidatesN = 100
    generations = 1000
    mutation_rate = 0.05
    inactivity_max = 100
    threshold = 0

    models = [DTLZ1, DTLZ3, DTLZ5, DTLZ7]
    objectives = [2, 4, 6, 8]
    decisins = [10, 20, 40]
    model_names = {DTLZ1: 'DTLZ1', DTLZ3: 'DTLZ3', DTLZ5: 'DTLZ5', DTLZ7: 'DTLZ7'}
    
    hypervolume = {}

    for model in models:
        hypervolume[model_names[model]] = {}
        for objectivesN in objectives:
            hypervolume[model_names[model]][objectivesN] = {}
            for decisionsN in decisins:
                print 'Model: ', model, ' Objectives: ', objectivesN, ' Decisions: ', decisionsN
                hypervolume[model_names[model]][objectivesN][decisionsN] = []
                (mn, mx) = baselines(model, decisionsN, objectivesN, 100000)
                for sd in xrange(15):
                    pareto_frontier = GeneticAlgorithms(model, decisionsN, objectivesN, sd, candidatesN, generations, mutation_rate, inactivity_max, threshold)
                    hypervolume[model_names[model]][objectivesN][decisionsN].append(hveval(pareto_frontier, mn, mx, 100000))

    with open('hypervolumes.bin', 'wb') as f:
        pickle.dump(hypervolume, f)

    analyze_results(hypervolume, models, model_names, objectives, decisins)
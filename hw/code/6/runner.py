from __future__ import division
from random import randrange
from random import randint
from random import random
#from models import Schaffer
#from Schaffer import Schaffer
#from Golinski import Golinski
from SA import SA
from MaxWalkSat import MaxWalkSat
from DE import DE

import sys

def run(algorithm, model):
    if algorithm == "SA":
        algo = SA(model)
    elif algorithm == "DE":
        algo = DE(model)
    elif algorithm == "MaxWalkSat":
        algo = MaxWalkSat(model)
    print "Best State " + str(algo.run())
    print "Total Evaluations: " + str(algo.evals)    

for model in ["Osyczka", "Golinski", "Kursawe", "Schaffer"]:
    for algorithm in ["SA", "MaxWalkSat", "DE"]:
        print "===================================================================="
        print "Running " + algorithm + " for " + model
        run(algorithm, model)
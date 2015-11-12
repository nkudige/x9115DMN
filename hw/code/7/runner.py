from __future__ import division
from random import randrange
from random import randint
from random import random
#from models import Schaffer
#from Schaffer import Schaffer
#from Golinski import Golinski
from MaxWalkSat import MaxWalkSat
from DE import DE

import sys

def run(algorithm, model):
    if algorithm == "DE":
        algo = DE(model)
    elif algorithm == "MaxWalkSat":
        algo = MaxWalkSat(model)
    print "Best State " + str(algo.run())
    print "Total Evaluations: " + str(algo.evals)    

for model in ["Osyczka", "Golinski", "Kursawe"]:
    for algorithm in ["MaxWalkSat", "DE"]:
        print "===================================================================="
        print "Running " + algorithm + " for " + model
        run(algorithm, model)
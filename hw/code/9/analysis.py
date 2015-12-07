import numpy as np, pandas as pd, pickle
from DTLZ import *

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

if __name__ == '__main__':
    with open('hypervolumes.bin', 'rb') as f:
        hypervolume = pickle.load(f)

    models=[DTLZ1]
    objectives=[2]
    decisins=[10]
    model_names = {DTLZ1: 'DTLZ1', DTLZ3: 'DTLZ3', DTLZ5: 'DTLZ5', DTLZ7: 'DTLZ7'}

    analyze_results(hypervolume, models, model_names, objectives, decisins)
# x9115KMN
# CSC 591 - Automated Software Engineering

## Programming Assignment 6
* Differential Evolution (DE.py) is run for different models and the medians of the frontier are printed.

DE is run on the following models:
* Schaffer (Schaffer.py)
* Kursawe (Kursawe.py)
* Golinski (Golinski.py)
* Osyczka (Osyczka.py)

... that can be executed as follows:
* python DE_runner.py

## Is DE(s) useful?
* The median values in the frontier for different sampling(33%, 50%, 70%, 100%) rates indicate that the sampling rate doesn't affect 
the median of results of the state energies in the frontier. Thus when the algorithm is run with lower value of s, it takes lesser time
to execute. This means that DE(s) is would be useful in optimizing the search for best state.


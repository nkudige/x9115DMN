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

## Screenshots
###### Note: Screenshots have been added for DE on Golinski model with 33%, 50%, 70% and 100% elite sampling. However, executing the program as specified above will produce the output for these elite sampling rates for all 4 models mentioned.

### DE - Golinski - 33% sampling rate
![DE - Golinski - 33% sampling rate](https://cloud.githubusercontent.com/assets/4932677/11171895/6da9c1f4-8bc9-11e5-93e0-fc9b0a45dcc6.PNG)

### DE - Golinski - 50% sampling rate
![DE - Golinski - 50% sampling rate](https://cloud.githubusercontent.com/assets/4932677/11171897/6dab925e-8bc9-11e5-945a-255479944d0e.PNG)

### DE - Golinski - 70% sampling rate
![DE - Golinski - 70% sampling rate](https://cloud.githubusercontent.com/assets/4932677/11171894/6d9f6740-8bc9-11e5-89db-cb0988390e62.PNG)

### DE - Golinski - 100% sampling rate
![DE - Golinski - 100% sampling rate](https://cloud.githubusercontent.com/assets/4932677/11171896/6daa7c66-8bc9-11e5-8c8a-b75a8376c155.PNG)
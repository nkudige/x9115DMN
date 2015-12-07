
# Code 9 - Report

#####Group Members:

- Deepak Nandihalli (drnandih)

- Madhura Rajopadhye (mrajopa)

- Nithanth Kudige (nkudige)

### I. Abstract

Genetic Algorithms (GA) are inspired by the mechanism of natural selection, a biological process in which stronger individuals are likely to be the winners in a competing environment. A positive value, generally known as the fitness value, is used to reflect the degree of "goodness" of an individual for solving the problem, and this value is closely related to the individual's objective value.[1] Genetic Algorithms are evolutionary algorithms that may be used to solve search and optimization problems. In this project, we use GA to optimize the DTLZ1,3,5,7 models with 2,4,6,8 objectives and 10,20,40 decisions.

### II. Introduction

	Genetic Algorithms simulate the process of natural selection and survival of the fittest. Each individual in a population has an associated fitness score that is an accurate representation of that individual's "goodness" in the society. The higher the fitness score of an individual, the more "fit" he is considered to be. Individuals that are fitter than others tend to have a natural advantage over the others in terms of survival and procreation. They are naturally selected over less fitter individuals, and thus have higher chances of "reproducing" to produce "children". These children, who come from two of the fitter parents, often acquire a lot of positive attributes from the parents, and may even develop attributes that neither of their parents exhibited, and are very likely to be even fitter than either of their individual parents. These children now compete with the rest of the society (including their parents), and sadly, one of the senior members in the society may have to make way for these younger, fitter, children if they are found to be less fit than the children. This process continues for several generations and over a long period, the future generations generally tend to be much fitter than the older generations.

	In the scenario briefed above, there are 3 main algorithms at work, namely:
	- Selection: This is where fitter individuals of a society are naturally more likely to survive than the others.
	- Crossover: This is the part where two "selected" individuals in the society reproduce and bring to the world a brand new child of theirs. This child naturally inherits several qualities from both its mother and its father.
	- Mutation: This explains how a new-born child may possess certain qualities that neither of its parents possess. At some probability, the certain characteristics obtained from the child's parents may "mutate" and result in something neither of its parents possessed.

	We make use of these 3 algorithms to generate several 'generations' of solutions to the DTLZ models; presumably producing better and better solutions as the generations progress.

	The rest of the paper is organized as follows - Section III discusses the implementation details and some of the design choices made during the course of implementation. Section IV provides a summary of our interpretation of the results obtained when GA was tested against DTLZ 1, 3, 5, 7. Section V talks about the threats to the validity of our implementation while Section VI talks about our learnings from this implementation and our plans to better the algorithm. Section VII is references.

### III. Implementation

 - **Optimization** is the main focus at hand. We aim to use our GA algorithms to derive the best possible decisions (10, 20 and 40) such that the objectives are maximized.
 - **Multi-objective optimization**: We consider multiple objectives (2, 4, 6 and 8). When there are conflicting objectives, the decisions must be selected optimally.

 To begin with, a random population of size 100 (default population size) is generated.

 Next to follow are the following steps in that order - selection, cross-over and mutation. We go over our implementation of each briefly.

 ##### Selection
 From the population generated, we select all candidates in the pareto frontier by performing a binary domination comparison between each candidate and every other candidate in the population. These candidates in the pareto frontier are the 'selected' candidates. These are also initially set as the 'best' candidates.

 ##### Cross-over
 Randomly select two parents from the pareto frontier with replacement (which means the two parents could be the same). Further, we select a random 'crossover point'. Next, we select all decisions up to the crossover point from the daddy, and all decisions starting from the crossover point from the mummy. We combine these to produce a baby.

 ##### Mutation
 A mutation rate is fixed (0.05 default). This is the probability at which each of the decisions of the baby produced in the previous step could be 'mutated' - randomly generated - into a brand new decision. That is, there is effectively a 5% chance that any given decision in the baby is randomly mutated.

 After the baby undergoes the steps outlined above, it is added to the 'next generation'. 100 (the default population size) babies are created in the exact same way from the previous generation's parents. They comprise of the 'new generation'. The pareto frontier of the new generation is now calculated, and the candidates in the pareto frontier form the 'selection' for that generation. The cycle thus continues.

 After each generation's pareto frontier is identified, the candidates in the frontier must then face-off against the current 'best' candidates. The ones who binary-dominate all other candidates get to stay in the group of 'best candidates', and the others are kicked out.

 There are two possible ways that the new generation production could be stopped. It is automatically stopped after 1000 generations (default), but there is also a chance that it may stop earlier. The early termination condition employed by us is as follows: after every 100 generations, compare the best candidates with the best candidates from a 100 generations ago. If there is no change in this 'best' frontier, then we terminate immediately.

### IV. Observations & Results

There is no general consensus on how a set of pareto frontiers in a multi-objective optimization problem can be compared against one another. This is still a heavily researched topic with no single conclusion. In this project, we use the hypervolume of a pareto frontier as an indicator of its quality. This is a normalized value in the range 0 - 1; 1 being the best score and 0 being the worst. 

We look at three different statistics concerning the hypervolume of the best pareto frontier obtained - the mean, the median, and the inter-quartile range. In the screenshot attached, we produce these statistics for each of DTLZ1,3,5,7 individually. The rows indicate the number of objectives and the columns indicate the corresponding number of decisions. The values found under these rows and columns are the mean, the median and the interquartile range respectively.

[screenshots]

### V. Conclusion

### VI. Threats to Validity

- **Validity of Conclusion**: We believe the conclusions are quite sound. We ran our algorithm for up to a 1000 generations with a fairly large every-100-generation evaluation to check for early termination possibility. We have also performed 15 repitions for each model, thus producing fairly consistent results.
- **Comparison method**: Binary domination may not always work as well as we expect it to. Consider a not-so-common scenario where no candidate binary-dominates another candidate in the population. In such cases, how do we determine who the fittest individuals are?
- **Evaluation Method**: As discussed earlier, we use the hypervolume as a metric of "goodness" of the best pareto frontier found. While this seems to be a promising approach, there is still much debate and ongoing research in this area.

### VII. Future Work

- Try out the continuous domination method rather than binary domination and see if that results in better results.
- Implement clever techniques and heuristics to speed up the code where applicable.
- Tune the parameters of GA and see how it turns out.
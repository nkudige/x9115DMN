#CODE 10 - Review

#####Group Members:

- Deepak Nandihalli (drnandih)

- Madhura Rajopadhye (mrajopa)

- Nithanth Kudige (nkudige)

### I. Abstract

<p>Differential evolution is a type of evolutionary computation that allows us to move to optimized solutions using some measure of quality. A large amount of research is being conducted to use this algorithm to optimize the parameters of other algorithms which also belong to the class of evolutionary algorithms, like the genetic algorithm. The algorithms generate solutions to optimization problems using techniques inspired by natural evolution, such as inheritance, mutation, selection, and crossover. [1] </p>
<p>In this code and review, we aim to utilize the concepts of differential evolution in order to optimize the parameters of genetic algorithms.</p>

### II. Introduction
<p>Genetic algorithms as well as differential evolution, as stated above, belong to a bigger class of algorithms called evolutionary algorithms which is a generic population-based metaheuristic optimization problem. [2] </p>
<p>Genetic Algorithms simulate the process of natural selection and survival of the fittest. Each individual in a population has an associated fitness score that is an accurate representation of that individual's "goodness" in the society. The higher the fitness score of an individual, the more "fit" he is considered to be. Individuals that are fitter than others tend to have a natural advantage over the others in terms of survival and procreation. They are naturally selected over less fitter individuals, and thus have higher chances of "reproducing" to produce "children". These children, who come from two of the fitter parents, often acquire a lot of positive attributes from the parents, and may even develop attributes that neither of their parents exhibited, and are very likely to be even fitter than either of their individual parents. These children now compete with the rest of the society (including their parents), and sadly, one of the senior members in the society may have to make way for these younger, fitter, children if they are found to be less fit than the children. This process continues for several generations and over a long period, the future generations generally tend to be much fitter than the older generations.[4]</p>
<p>In the scenario briefed above, there are 3 main algorithms at work, namely:</p>
- **Selection**: This is where fitter individuals of a society are naturally more likely to survive than the others.
- **Crossover**: This is the part where two "selected" individuals in the society reproduce and bring to the world a brand new child of theirs. This child naturally inherits several qualities from both its mother and its father.
- **Mutation**: This explains how a new-born child may possess certain qualities that neither of its parents possesses. At some probability, the certain characteristics obtained from the child's parents may "mutate" and result in something neither of its parents possessed.
<p>Differential evolution consists of the following main steps:[3]</p>


![alt tag](http://i.imgur.com/e7H0jyI.png?1)



<p>In this project, we would like to utilize differential evolution for the purpose of tuning the parameters of genetic algorithm. The advantage of using differential evolution is that it doesn’t require the objective function to differentiable or continuous making this algorithm applicable to a wider variety of applications. </p>

### III. Implementation
The genetic algorithm used for this purpose is largely from our Code 9 implementation which has been summarized as below:[4] 
<ul>
<li> <b>Selection</b>: The pareto frontier is evaluated through performing binary domination and these are the selected candidates which are also set as the initial set of best candidates</li>
<li> <b>Crossover</b>: With some probability, two random candidates are selected and a random crossover point is selected. All decisions until the crossover point are attributed to the first parent and the ones after the crossover point are attributed to the mother. These are combined to generate an offspring.</li>
<li> <b>Mutation</b>:  We want to mutate some decisions in the offspring. According to the rate of mutation, we select some decisions and randomly modify it. </li></p> 
</ul>
<p>Once an offspring is formed, it is dropped in the pool of candidates and we continue the above three steps. Each candidate in the pareto frontier is compared with the set of best candidates and according to binary domination, the set is modified by replacing the ones that lose. </p>
<p>If we observe this algorithm, there are various aspects whose value is left to the intelligence of the programmer to finalize. These are aspects such as number of iterations of the algorithm, rate of mutation, probability of randomly choosing candidates for crossover, number of candidates. </p>
<p>We find the optimized values for each of these using the differential evolution algorithm.<p>

<p>Hence, we proceed in the following fashion:[3]
<ol>
<li>For a given parameter set of D parameters, let N be the population size, the parameter vector will have the form xi, G  = [x1,G, x2,G…xD,G] where i= 1 to N and G is the generation number</li>
<li>Define the domain, i.e. upper/lower bounds xLj ≤ xj,i,1 ≤ xUj on values that the parameter can take</li>
<li>Select initial parameter value uniformly over the interval [xLj, xUj]</li>
<li>Each of the N parameter vectors undergo mutation, recombination and crossover</li>
<li>For a given parameter vector, randomly select three different vectors
<ul>
<li>Add the weighted difference of two of the vectors to the third with some mutation factor F. The resulting vector is called the donor vector</li>
<li>With some probability CR, combine elements of the donor vector to the target vector xi,G to result in the trial vector</li>
<li>Target vector is compared to the trial vector and their goodness is evaluated using a fitness function and the winner goes on to the next generation</li>
</ul></li>
<li>The process is repeated until a given stopping criterion is satisfied </li>
<li>We utilize the resulting solution as parameter values for the genetic algorithm </li>
</ol>
</p>

### IV. Results
[Screenshots]

### V. Conclusion

### VI. Threats to Validity
- **Comparison method**: Binary domination may not always work as well as we expect it to. Consider a not-so-common scenario where no candidate binary-dominates another candidate in the population. In such cases, how do we determine who the fittest individuals are?
- **Evaluation Method**: As discussed earlier, we use the hypervolume as a metric of "goodness" of the best pareto frontier found. While this seems to be a promising approach, there is still much debate and ongoing research in this area.


### VII. References:
<ul>
<li>[1] https://en.wikipedia.org/wiki/Genetic_algorithm</li>
<li>[2] https://en.wikipedia.org/wiki/Evolutionary_algorithm</li>
<li>[3] http://metodosestadisticos.unizar.es/asignaturas/62801/DiferentialEvolution.pdf</li>
<li>[4] https://raw.githubusercontent.com/nkudige/x9115DMN/master/hw/code/9/README.md</li>

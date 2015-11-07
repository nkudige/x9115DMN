# Paper 5 - Summary

## Reference
A systematic review of search-based testing for non-functional system properties
Wasif Afzal *, Richard Torkar, Robert Feldt
Department of Systems and Software Engineering, School of Engineering, Blekinge Institute of Technology, S-372 25 Ronneby, Sweden

## Keywords

1. **Search based testing** - Search-based software testing is the application of metaheuristic search techniques to generate software
tests
2. **Systematic review** - A systematic review is a process of assessment and interpretation
of all available research related to a research question or subject
of interest
3. **Non-functional properties** - Execution time, Safety, Quality of Service, Security


## Artifacts:

1. **Checklists** - There are research questions which the authors hope to explore in the literature related to software testing using search based techniques for non-functional properties:
  * In which non-functional testing areas have metaheuristic search techniques been applied?
        ** What are the different metaheuristic search techniques used for testing each non-functional property?
        ** What are the different fitness functions used for testing each non-functional property?
        ** What are the current challenges or limitations in the application of metaheuristic search techniques for testing each non-functional property?

2. **Study instruments** - The population in this study is the domain of software testing. Intervention includes application of metaheuristic search techniques to test different types of non-functional properties.

3. **Results** - In general the authors found that genetic algorithms to be the most widely used technique with 21 papers referring it. The results related to each of the non-functional property is as follows:
    Metahueristic is a ' * ' represents the most widely used for the given non-functional property
    <table>
    <thead>
    <b>
    <td> Non-functional property </td><td> Metaheuristic </td><td> Fitness Function </td>
    </b>
    </thead>
    <tr>
    <td> Excecution time </td><td> *Genetic algorithm, extended genetic algorithm, simulated annealing </td><td> exceuction time in terms of processor cycles or time units, coverage of code annotation </td>
    </tr>
    <tr>
    <td> Quality of service </td><td> *Genetic algorithm </td><td> Based on the maximization of desired QoS attributes while minimizing others, including a static or dynamic penalty function, Combination of distance based fitness that rewards solutions close to QoS constraint violation with a fitness guiding the coverage of target statements </td>
    </tr>
    <tr>
    <td> Security </td><td> *Genetic algorithm, Grammatical evolution, Linear Genetic Programming, Particle Swarm Optimization </td><td> Fitness function based on the configuration of registers and stack,  fitness functions covering vulnerable statements, maximum nesting level and buffer boundary, etc </td>
    </tr>
    <tr>
    <td> Usability [array construction] </td><td> Tabu search, *Simulated annealing, Hill climbing, genetic algorithm, Ant colony algorithm </td><td> Number of uncovered t-subsets </td>
    </tr>
    <tr>
    <td> Safety </td><td> Genetic algorithm, simulated annealing </td><td> Cost related to the violation of the safety property and achievement of dangerous situation, Evaluation of different branch predicates with zero cost if the safety property evaluates to false and positive cost otherwise </td>
    </tr>
    </table>
4. **Future work** - The authors outlines various areas with potential for future work. These mainly refer to exploring aspects of performance, scalability, resulability of t-combinations and further research into use of ant colony algorithms 

## Areas of improvement
There are 4 threats to validity outlined by the authors namely:
 * **Conclusion validity**: This refers to biasness in applying quality assessment and data extraction
 * **Internal validity**: Internal validity, according to the authors, arises from unpublished research that had undesired outcomes or proprietary literature that is not made available
 * **Construct validity**: May arise due to exclusion of relevant studies
 * **External validity**: This occurs due to generalization of results outside the scope of study

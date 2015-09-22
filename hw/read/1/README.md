#Paper 1 - Summary

##Reference:
Nadia Alshahwan and Mark Harman (2011).  
"Automated Web Application Testing Using Search Based Software Engineering"  
*Automated Software Engineering (ASE), 2011 26th IEEE/ACM International Conference*, 3-12.  
[Link](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6100082)

##Keywords:
* ii1. **Search Based Software Engineering**: An approach that reformulates software engineering problems into optimization problems
* ii2. **Alternating Variable Method**: This is the process of making changes to one input variable while fixing all other variables. Branch distance is measure to determine how close an input comes to covering the traversal of a desired branch. If changes affect branch distance, AVM applies a larger change in the same direction.
* ii3. **Near Miss Seeding**: For each work list branch, input vector is mutated iteratively until the branch is covered. At each iteration, input values that cause near misses are tracked. Near miss is a input vector that causes fitness improvement for a branch other than the targeted branch. Near misses are used in place of random values, when initializing a search to cover a branch. This approach is called Near Miss Seeding.
* ii4. **Dynamically Mined Values**: Seeding values dynamically during execution into the search space is called Dynamically Mined Value.

##Artifacts:
* iii1. **Motivational Statements**: The paper addresses as to why the testing of web applications is critical. The internet user numbers has grown by 400% over the past ten years. The online retail sales has grown by 11%. These web applications demand high availability. As web technologies keep changing frequently and their adopters seek early acquisition of market, the development time squeezes the testing phase. This introduces the need for automating the tests when Search Based Software Testing is used. Popular web development languages such as PHP and Python have characteristics that pose a challenge when applying search based techniques such as dynamic typing and identifying the input vector. The unique and rich nature of a web application’s output can be exploited to aid the test generation process and potentially improve effectiveness and efficiency.
* iii2. **Hypothesis**: 
 - first automated search based approach to web application testing.
 - Use of dynamically mined values significantly increases coverage in all applications studied and also reduces effort in testing. These results may prove useful for other SBST paradigms.
* iii3. **Statistical tests**: For evaluation, the same PHP applications used by other research using non search based approach was used. Each of the 3 versions of the tool were ran 30 times on each of the 6 PHP applications and collected coverage data. With 30 runs of each algorithm, a sufficient sample size for statistical significance testing is provided. The tool was executed on an Intel Core 2 Duo CPU, running at 2 GHz with 2 GB RAM. For each of the 6 Web applications, a graph of branch coverage vs approach & Faults vs approach is plotted.
* iii4. **New Results**: Based on the empirical evidence from the experiments: 
 - Each enhancement improved branch coverage for all of the 6 applications under test. DMV statistically significantly outperforms NMS and SCS for all 6 applications studied. SCS achieved higher coverage than NMS for all 6 applications.
 - Effort decreases significantly by using SCS rather than NMS for all applications except one.
All these results show that test generation process for testing web application can significantly reduce the effort and improve the branch coverage for web application testing.

##Areas of Improvement:
* iv1. The paper doesn’t provide proper reasoning as to why those specific web applications were selected for the empirical analysis. The paper should have provided the criteria for selecting the web applications for testing their Automated Search Based Testing tools for web applications.
* iv2. The paper doesn’t clearly explain about what the branch coverage results were compared to. It just compares the results within the three models built, but it doesn’t compare it with manually written tests. Comparing with manually written tests would have been a good baseline for branch comparison & for identifying errors.
* iv3. This paper misses identifying what future work could be done to get rid of the limitations that are mentioned and also on how to further improve the efficiency, coverage, usability and fault finding abilities of the methods used.
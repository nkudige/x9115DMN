# Paper 9 Review

## Reference
	
Saswat Anand , Edmund K. Burke , Tsong Yueh Chen , John Clark , Myra B. Cohen , Wolfgang Grieskamp , Mark Harman , Mary Jean Harrold , Phil Mcminn, 
An orchestrated survey of methodologies for automated software test case generation, Journal of Systems and Software, v.86 n.8, p.1978-2001, August, 2013

##Keywords
  1. **Symbolic execution**: Symbolic execution is a program analysis technique that analyzes a program’s code to automatically generate test data for the program.
  2. **Model-based testing**: Model-based testing (MBT) is a light-weight formal method which uses models of software systems for the derivation of test suites.
  3. **Combinatorial testing**: It consists of selecting a sample of input parameters (or configuration settings), that cover a prescribed subset of combinations of the elements to be tested
  4. **Adaptive Random testing**: It refers to the family of testing methods in which test cases are random and evenly spread across the input domain
  5. **Search based testing**: Search based software testing (SBST) is a branch of search based software engineering (SBSE), in which search algorithms are used to automate the process of finding test data that maximises the achievement of test goals, while minimising testing costs
  
## Artifacts
  
  1. **Motivational Statements**: Software testing is indespensable for software development which has made the test case generation an important software artifact. The test cases must be exhaustive and should effeciently serve the purpose of testing. Hence, the authors explore various types of automated test case generation techniques. 
  2. **Results**: The results have been summarized as follows:
    - <i>Test data generation by symbolic execution</i>: It uses program analysis and constraint solvers. This method can be used in combination with other methods. This technique has various open problems - path expolsion, path divergence and complex constraints. Though solutions ot these problems exist, more research is needed so that this technique can applied to real-world problems. 
    - <i>Test data generation by model-based testing</i>: MBT, unlike traditional methods, does not use formal models for verification, it makes use of insights in the correctness of a program. It encompasses various approaces like axiomatic approaches, FSM approaches and labelled transition system approaches. A variety of notations are used for describing models like scenario-oriented, process-oriented and state-oriented. There are various tools available for carring out model-based testing lile Conformiq designer, Smartesting Certifylt and Spec Explorer.   
    - <i>Test data generation in combinatorial testing</i>: CIT has traditionally been used as a specification-based, system testing technique to augment other types of testing. It is meant to detect one particular type of fault; those that are due to the interactions of the combinations of inputs or configuration options. There has been an increase in the number of algorithms that generate CIT samples. More and more applications make use of this technique. The authors feel that this is a promising area of research for automated test case generation.
    - <i>Test data generation by adaptive random testing</i>: This is the only feasible technique present if the source code is unavailable and the specifications are incomplete. Adaptive random testing is an enhancement of random testing. There are many approches that have been developed to implement the concept of ART (spreading of test cases over the input domain) like selection, exclusion, partitioning, test profiles, metric-driven, etc. Measures of effectiveness for ART include P-measure, F-measure, time to detect first failure, etc. These use more computation time and memory as compared to random techniques.
    - <i>Test data generation in search-based software testing</i>: The techniques make use of various search algorithms to come up with test cases and evaluate them using a fitness function. The definition of this fitness function is a major concern. This approach is widely used due to its applicability to any test objective.  

## Areas for improvement
The authors highlight that there is much research that can be carried out in each of the test data generation techniques. However, empirically stating the comparision between ech of the techniques is one area for improvement. 

#Paper 4 Summary

#Reference
Automated Identification of Parameter Mismatches in Web Applications
William G.J. Halfond and Alessandro Orso
College of Computing
Georgia Institute of Technology
{whalfond, orso}@cc.gatech.edu


##Keywords:

ii1. **Parameter mismatch**:
root method of web application:
When a web component A communicates with another component B, it does so by sending a request to B that invokes one of B’s interfaces and provides a set of arguments in the form of name-value
pairs. An error in this communication can occur for several reasons: B may expect additional arguments, A or B may refer to the same argument by different names, or A may send too many arguments. We call these types of errors parameter mismatches.

ii2. **HTML Fragment Resolution**:
The process of HTML fragment resolution determines the HTML content contributed by a given node of a web component. This method takes a node n as input and returns a set of strings (possibly with placeholders) that represent the HTML fragments contributed by the node. The node n can either write data to output stream or calls a method that is associated with a summary. 
When n writes to a output stream, resolve runs string analysis on the output. If n calls a method with a summary, resolve retrieves the summary associated with the the target method of n & runs string analysis on the corresponding arguments provided by the callsite and replaces the placeholders withe result of string analysis.

ii3. **Intermediate Parsing**:
Intermediate parsing reduces the amount of string data that must be stored and propagated by the analysis. This method takes an HTML fragment as input and returns an HTML fragment in which irrelevant tags have been removed.
The motivation for using intermediate parsing is that storing all HTML fragments that can be generated by a component creates a high memory overhead for the analysis. Motivation behind this is that HTML fragments contain tags that do not affect interface invocations and are only used to display text or enhance web page.

ii4. **Interprocedural Connected Flow Graph** :
This is a graph of the web application, where each node is a component\procedure and edges represent the interaction between each of the components or procedure invocations by components.

##Artifacts:

iii1. **Motivation**:
The components of a web application communicate extensively in order to provide a feature-rich environment. These components integrate content and data from multiple data sources. This process of gathering data from multiple sources involves sending requests with parameters in the form of name value pairs. The complexity of inter-component communication, generation of interface invocations and definition of accepted interfaces occur at runtime, makes these errors more probable. Such errors can be serious and can cause a component to fail unexpectedly.

iii2. **Limitations**:
Assumption that all paths are feasible: The technique described in the paper assumes that all the paths are feasible in a given application. Thus the algorithm generates a set of HTML pages that could be generated by a component and interface invocations that could not occur at run time.
Use of Javascript:
The current implementation doesn't do the javascript analysis of the web pages. The Javascript code could add or remove a name value pair to an invocation before it is performed. So this method fails for applications which have Javascript modifying the parameters for method invocation.


iii3. **Future work**:
Web Application Interface Verification Engine(WAIVE): The analysis run by WAIVE had to track a huge number of distinct page fragments that related to interface invocations. Most time consuming part was processing done by external libraries such as for building call graphs and flow graphs for string analysis. There were Out of memory errors generated due to large number of HTML fragments generated that exceeded heap memory allocated for JVM. Resolving these errors and optimizing the external libraries are part of the future work.

iii4. **Related Work**:
Web Application Interface Verification Engine(WAIVE): The analysis run by WAIVE had to track a huge number of distinct page fragments that related to interface invocations. Most time consuming part was processing done by external libraries such as for building call graphs and flow graphs for string analysis. There were Out of memory errors generated due to large number of HTML fragments generated that exceeded heap memory allocated for JVM. Resolving these errors and optimizing the external libraries are part of the future work.

iii4. **Related Work**:
- A technique by Ricca and Tonella that allows developers to use UML to mdel links and interface elements of each page in a web application.
- Betin-Can and Bultan provide a more expressive modelling language that allows developers to represent dynamic interactions between components in a web application.
- Deng, Frankl and Wang model a web application by scanning its code and identifying links and names of input parameters
All these approaches include only static analysis of the code used to validate the syntactical structure of the generated HTML pages and cannot identify parameter mismatches in web applications

##Areas of improvements:

(iv1.) The paper does not justify as to why those 4 web applications were chosen over the others for analysis.
(iv2.) 
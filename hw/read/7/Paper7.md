# Paper 7 Summary

## Reference
Serdar Doğan , Aysu Betin-Can , Vahid Garousi, 
Web application testing: A systematic literature review, Journal of Systems and Software, 91, p.174-201, May, 2014

## Keywords
1. **Systematic Literature review**: A systematic review is a process of assessment and interpretation of all available research related to a research question or subject of interest
2. **Web Application Testing**: Techniques used to test functionalities of applications hosted on the web
3. **Functional testing**: Testing that verifies the workflow of the web application 

##Artifacts

1. **Motivational Statements**: Since the area of functional testing is constantly growing and maturing dynamically with increasing number of papers being published in the field, the authors feel it is important to systematically identify, analyze, and classify the publications and provide an overview of the trends and empirical evidence in this specialized field.

2. **Checklists**: The main reseach questions that the authors aim to addres in the paper are as follows:
 * What types of test models, fault models and tools have been proposed?
 * How are the empirical studies in WAT designed and reported?
 * What is the state of empirical evidence in WAT?
 
3. **Related work**: 
  * Secondary studies in software testing - 24 studies were found which were of varies categories like SLR, SM, taxonomies, survery/analysis, literature review
  * Online paper repositories in software engineering - Authors address that the online repositories are reported to supplement secondary studies. This is a by-product of increading SLRs and SMs.
  * Secondary studies in web application testing -  Authors list various secondary studies in this field of WAT like Kam and Dean, 2009; Alalfi et al., 2009; Lucca and Fasolino, 2006; Amalfitano et al., 2010b.
  
4. **Results**: Each of the research questions had several sub-questions which were addressed. The findings are summarized as follows;
  * RQ1: 
    - A large number of studies (40, 42%) proposed test techniques which used certain models as input or inferred (reverse engineered) them. The models can be classified as navigation models, control and data flow models and, DOM models, etc. Navigation models were found to be the most popular followed by DOM models.
    - Different bug/fault taxonmies related to web applications were found to be proposed in various primary studies like authentication/permission, internationalization, functionality, database persistence
    - Various studies reference tools that support web application testing (54%). The more recently pushlished studies (2008 and later) reference tools that are available for download which the authors reckon is a good sign. Some of the tools presented were MBT4Web, MUTANDIS, ATUSA, Crwaljax, etc which are available for download
  
  * RQ2:
    - Different metrics used for assessing cost and effectiveness of WAT techniques are - cost metrics: effort/test time, test-suite size, memory space and others related to complexity) and effectiveness metrics: code coverage, detecting injected faults model-based requirements coverage, etc.
    - Sometimes mutiple metrics or pairs of metrics were found to be used 
    - Various validity threats are found to question the validity of these research studies. External validity was found to be most common threat identified by various papers. Validation research facet of empirical studies succeeded to identify only 51% of the threats posed in thier studies
    - Most of the empirical studies have outlined the context of their studies where a reader can compare it with other studies and the study design has been explained well
    - Most of the studies were performed in a laboratory setting while some in industrial setting. However, none of the studies used methods relevant to the practitioners.
    
  * RQ3:
    - Three of the empirical studies studied scalability and reported corresponding evidence 
    - Empirical studies reported carrying out comparisons with other studies/tools. Highest of these kind of comparision was session based testing.
    - 62& studies target server side application, 45% target client side application and only 5% provide empirical results of both sides of a web application
    
## Areas for improvement
Authors highlight that there are different terms for web application testing and analysis with many alternatives and different combinations. However, the list that the authors came up with might not be exhaustive which can result in reduction in number of papers found
  
    - 

# Overview

Given a string of hydrophobic and hydrophilic amino acids, this program is meant to construct a SAT problem, which can then be solved with a SAT solver.
The output format will be in DIMACS CNF, information on it can be found here. 
http://www.satcompetition.org/2009/format-benchmarks2009.html
1's will be the water lovers, 0's the water haters. I refer to each number in the input string as an amino acid. As such, the string "1001" has 4 amino acids.

## Rules
There are several rules that must be implemented in SAT problem, they are as follows.
1. No two amino acids can be placed within the same grid spot.
2. Each amino acid must be placed sequentially, except for the first. 
3. Each amino acid must be placed adjacent to the previously placed acid, again, except for the first.
4. The grid size is n^2, where n is the length of the input
After such, we create SAT logic that we include that 'counts' the matchings. Variables within the SAT logic reprents the total number of possible matchings. Prof. Gusfield suggested that this gone be done in a certain way. See the PDF for details
## Goal
1. Maximize the number of adjacent 1's, that are not adjacent in the input string.
In addition, there should be no post-processing. The SAT solver should be able to give a readable number, or variable, which can be numbered as variables, or a script can handle scraping the data appropriatley.

### Roadmap
- [x] Implement the rules that are stated above.
- [] Implement the counting that needs to be done. (Partially complete)
What needs to be done, is the ACTUAL counting. Some logic is broken. While salvaging is probable, re writing could be easier.
- [] Create a script that can automate the testing.



#### Authors
Chase Maguire, UC DAVIS 2018 with Prof. Daniel Gusfield.

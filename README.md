# Overview

Given a string of hydrophobic and hydrophilic amino acids, this program is meant to construct a SAT problem, which can then be solved with a SAT solver.
The output format will be in DIMACS CNF, information on it can be found here. http://www.satcompetition.org/2009/format-benchmarks2009.html
1's will be the water lovers, 0's the water haters.

## Rules
There are several rules that must be implemented in SAT problem, they are as follows.
1. No two amino acids can be placed within the same grid spot.
2. Each amino acid must be placed sequentially
3. Each amino acid must be placed adjacent to the previously placed acid.
4. The grid size is n^2, where n is the length of the input
## Goal
1. Maximize the number of adjacent 1's, that are not adjacent in the input string.
In addition, there should be no post-processing. The SAT solver should be able to give a readable number, or variable, which can be numbered as variables.

#### Authors
Chase Maguire, UC DAVIS 2018 with Prof. Daniel Gusfield.


"""Written in python 3.6"""
# Getting input
i = list(input("Enter input string \n"))
# Slice the input into a list
# A count of how many variables we have
varcount = 0
"""Placement rules"""

# Let there be a variable, X(i,j), is either 1 or 0; true or false, if character I is placed in position J
# i goes from 1 to n, j goes to  1 to n^2
j = []
for x in range((len(i)*len(i))):
    j.append(x)

'''Rule 1; Each acid must be placed'''

# Each spot needs to be placed
# Creation of X(i,j) represented as a 2d array
# We just need to specify that each i will be placed eventualy
# So, for every possible combination of i and j, we need to create a variable x.
# So this will be i * j big. so n^3 big 
# (or of all possible postions for 1) ^ (or of all possbile possitions for 2) ^ .... (or of all possbile for i)
#
# Matrix = [[0 for x in range(w)] for y in range(h)] 
# First array slice denotes the place in the grid, second denotes the place in the input string 
Mat = [[0 for x in range(len(i))] for y in range(len(j))]
#print(Mat)
# for each place in the grid, for each position, create the placement rule
# Creating a way to store each on of these placement rules
placementlist = []
for x in range(len(i)):
    varcount = 0
    currentlist = []
    for y in range(len(j)):
        # Need to generate a new variable here
        varcount = varcount + 1
        currentlist.append(varcount)
    currentlist.append(0)
    placementlist.append(currentlist)
print(placementlist)
# Now, each slot j has i variables 'assigned' to it. 
# Just needs to be written to the file, but this is the last step
''' One acid per grid '''
# Should be something such as 
# For each j, for each i
#  

''' Rule 3, each acid must be placed adjacent to the previously placed one. The first is the exception '''
# For i, but not the first
# i+1 must be in either
#   the grid to the bottom, top , left, or right
#   Exceptions are on the edges.
# Corners are 0, n, n^2, n^2-n


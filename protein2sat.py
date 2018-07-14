
"""Written in python 3.6"""
#Getting input
i = list(input("Enter input string \n"))
#Slice the input into a list

"""Placement rules"""

'''Rule 1; no two acids in the same slot of the grid'''
#Let there be a variable, X(i,j), is either 1 or 0; true or false, if character I is placed in position J
#i goes from 1 to n, j goes to  1 to n^2
j = []
for x in range((len(i)*len(i))):
    j.append(x)

print(i)
print(j)
# Each spot needs to be placed
# Creation of X(i,j) represented as a 2d array
# We just need to specify that each i will be placed eventualy
# So, for every possible combination of i and j, we need to create a variable x.
# So this will be i * j big. so n^3 big 
# (or of all possible postions for 1) ^ (or of all possbile possitions for 2) ^ .... (or of all possbile for i)
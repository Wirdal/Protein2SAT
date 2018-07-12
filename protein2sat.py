
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
#Need to make an X(i,j) still
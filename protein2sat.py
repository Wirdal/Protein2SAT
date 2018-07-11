
"""Written in python 3.6"""
#Getting input
stringin = int(input("Enter input string \n"), base = 2)
#Slice the input into a list

"""Placement rules"""

'''Rule 1; no two acids in the same slot of the grid'''
#For each input string, for each grid square, only one input is allowed 
#Something along the lines of 1, -2, -3, but somehow placed in each grid location,
#Have variables for each grid location, numbered sequentially
#Same idea for each variable
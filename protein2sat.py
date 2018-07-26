
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
	currentlist = []
	for y in range(len(j)):
		# Need to generate a new variable here
		varcount = varcount + 1
		currentlist.append(varcount)
	placementlist.append(currentlist)
print(placementlist)
# Now, each slot j has i variables 'assigned' to it. 
# Just needs to be written to the file, but this is the last step
''' Rule 2, One acid per grid max '''
# For each possible pair of acids in each location, not both of those

# For each list
#   For each list + 1
#       For each elem in the first list
#          For each elem in the second list
#              Negate the two values, append them to list
uniquelist = []
for firstlist in range(len(placementlist)):
	# First list is getting slices of the placement list, except for the last
	if firstlist == len(placementlist) - 1:
		break
	else:
		for secondlist in range(len(placementlist[firstlist+1:])):
			secondlist = secondlist+firstlist+1
			for firstelem in placementlist[firstlist]:
				for secondelem in placementlist[secondlist]:
					uniquelist.append([-firstelem, -secondelem])
print(len(uniquelist))
''' Rule 3, each acid must be placed adjacent to the previously placed one. The first is the exception '''
adjacentlist =[]
for x in range(len(placementlist)):
	# Much like the previous one, however we only needs to look at one list and the
	# one that immediatley goes after it
	print(x)
	n = len(i)
	# So the first acid can be placed anywhere. So there are no restircitons
	# To where it goes
	# So we only need to go forward
	# We start at the first list, and create the edges for the first list

	# From 1 to n^2 - n + 1
	# Needs to get the last
	# WORKS
	leftedge = x[::n]
	# From 1 to n
	# WORKS
	topedge = x[:n]
	# from n to n^2 by n steps
	rightedge = x[n-1::n]
	# n^2 - n + 1 to n^2
	# A very lazy way of getting these, but it works
	x.reverse()
	bottomedge = x[:n]
	# To confirm by eye faster
	bottomedge.reverse()

	# Now we need to check if we're in the edge
	for y in x:
		localadjacencylist = []
		up = True
		down = True
		right = True
		left = True
		# Check if the elem we're checking is OK 
		if y in topedge: up = False
		if y in bottomedge: down = False
		if y in leftedge: left = False
		if y in rightedge: right = False
		
		# Now based on if the elem was in the, generate the rule
		# A -> B == B V -A
		# Where A is the placement,
		# B is the possible spots for the next acid
		if up:
			# -n
			localadjacencylist.append()
		if down:
			# +n
			localadjacencylist.append()
		if right:
			# +1
			localadjacencylist.append()
		if left:
			# -1
			localadjacencylist.append()

	print(leftedge, topedge, rightedge, bottomedge)
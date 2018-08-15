
"""Written in python 3.6"""
# Getting input
i = list(input("Enter input string \n"))
n = len(i)
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
#Mat = [[0 for x in range(len(i))] for y in range(len(j))]
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
# Now, each slot j has i variables 'assigned' to it. 
# Just needs to be written to the file, but this is the last step
''' Rule 2, One acid per grid max '''
# For each possible pair of acids in each location, not both of those
uniquelist = []
for index in range(len(placementlist)):
	firstlist = placementlist[index]
	try:
		rest = placementlist[index + 1 :]
	except IndexError:
		break
	for firstelem in firstlist:
			for secondlist in rest:
				uniquelist.append([-firstelem, -secondlist[firstlist.index(firstelem)]])
		# we've got all the pieces, just need to put it all together
	# Finish this
#For each list in the matrix
	# for each elem in the most recent list
		# For all other lists	
			# take the elem, and the same elem in the other lists and negate them

''' Rule 3, each acid must be placed adjacent to the previously placed one. The first is the exception '''
adjacentlist =[]
for x in range(len(placementlist)):
	
	try:
		firstlist = placementlist[x]
		# This is the one that should cause the index error
		secondlist = placementlist[x + 1]
	except IndexError:
		# Should be done if we get here
		break
	
	# Much like the previous one, however we only needs to look at one list and the
	# one that immediatley goes after it

	matsize = n**2
	# We also need to take care of the next things
	# So the first acid can be placed anywhere. So there are no restircitons
	# To where it goes
	# So we only need to go forward
	# We start at the first list, and create the edges for the first list

	# From 1 to n^2 - n + 1
	# Needs to get the last
	# WORKS
	leftedge = firstlist[::n]
	# From 1 to n
	# WORKS
	topedge = firstlist[:n]
	# from n to n^2 by n steps
	rightedge = firstlist[n-1::n]
	# n^2 - n + 1 to n^2
	# A very lazy way of getting these, but it works
	firstlist.reverse()
	bottomedge = firstlist[:n]
	# To confirm by eye faster
	bottomedge.reverse()
	firstlist.reverse()
	# Now we need to check if we're in the edge
	for y in firstlist:
		# We only need to go through the 
		localadjacencylist = []
		localadjacencylist.append(-y)
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
			# Just want to get the next matrix.
			# So we should only need to add my the square of n
			localadjacencylist.append((matsize + y) - n)
		if down:
			# +n
			localadjacencylist.append((matsize + y) + n)
		if right:
			# +1
			localadjacencylist.append((matsize + y) + 1)
		if left:
			# -1
			localadjacencylist.append((matsize + y) - 1)
		adjacentlist.append(localadjacencylist)

#print("ADj list", adjacentlist)
'''
All placement rules are done. We just need to do the rest of the rules
The next big one is how we define matches. We need to first define all possible
matches before we do anything else
'''
# What are the possible matchings, where do they come from?
# We need to look at every 1, and determine possible matchings from the rest of the string. 
# We won't need to look back, same kind of thinking as in 2.
# And we still have the same varcount, so we can just keep going from it
# But what are the placement rules? there must be some mathematical notation
# We need to find a formula
# Otherwise, we COULD create variables for everything, but that could be a big slowdown.
# No logical problems would be created though. This isn't a placement rule, just a matching one.
# But the basic logic for a matching should be
# 	Some 1, and some adjacent other 1, -> a matching variable
#	A -> B
#   (1 ^ 1 (another 1)) -> matching var
#   B V -A
#	matching var V (-1 V -1(another 1))
# NOTE this needs to be done for every possible pair that is next to the first 1
# Is it faster to compute at the high level where the next 1's could go?
# or is it faster to create variables willy nilly
# and let the cnf handle them?
# IT does not matter, we just simply need to go to 
# Grab the index of every single 1
indexlist = []
matchinglist = []
for x in range(len(i)):
	if i[x] == "1":
		indexlist.append(int(x))
print("index list", indexlist)
 # We have the indexes of all 1's. We can start to add from that
for x in indexlist:
	if x == indexlist[len(indexlist)-1]:
		break
	n1 = placementlist[x]
	leftedge = n1[::n]
	rightedge = n1[n-1::n]
	topedge = n1[:n]
	n1.reverse()
	bottomedge = n1[:n]
	bottomedge.reverse()
	n1.reverse()
	for y in indexlist[indexlist.index(x)+1:]: # the next elem in indexlist
	# x is the current, y is one after it
	# if distance between them is great enough and an even number
		if ((x + 3) <= y) and ((x+y +3) % 2) == 0:
			n2 = placementlist[y]
			for firstelem in n1:
				#if firstelem == n1[len(n1)-1]:
				#	break
				up, down, left, right = True, True, True, True
				# rules created here
				# we make a new clause for each possible placement
				if firstelem in topedge: up = False
				if firstelem in bottomedge: down = False
				if firstelem in leftedge: left = False
				if firstelem in rightedge: right = False
				if up:
					varcount = varcount + 1
					secondelem = n2[n1.index(firstelem) - n]
					matchinglist.append([varcount, -firstelem, -secondelem])
				if down:
					varcount = varcount + 1
					secondelem = n2[n1.index(firstelem) + n]
					matchinglist.append([varcount, -firstelem, -secondelem])
				if left:
					varcount = varcount + 1
					secondelem = n2[n1.index(firstelem) - 1]
					matchinglist.append([varcount, -firstelem, -secondelem])
				if right:
					varcount = varcount + 1
					secondelem = n2[n1.index(firstelem) + 1]
					matchinglist.append([varcount, -firstelem, -secondelem])
			else:
				pass
del indexlist
print(len(matchinglist))
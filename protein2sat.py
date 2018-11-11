

# Making this a global variable
# Only thing andHelper needs access to

def protein2sat(i):
	"""Written in python 3.6"""
	# Getting input
	name = i
	i = list(i)
	n = len(i)
	# Slice the input into a list
	# A count of how many variables we have
	"""Placement rules"""
	varcount = 0
	# Let there be a variable, X(i,j), is either 1 or 0; true or false, if character I is placed in position J
	# i goes from 1 to n, j goes to  1 to n^2
	j = []
	for x in range((len(i)*len(i))):
		j.append(x)

	'''Rule 1; Each acid must be placed'''
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
	''' Rule 2, One acid per grid max '''
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
		

		matsize = n**2
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

	'''
	All placement rules are done. We just need to do the rest of the rules
	The next big one is how we define matches. We need to first define all possible
	matches before we do anything else. There are two sides of an implication that need to be done
	'''

	'''
	Placement implies counting variable
	'''
	indexlist = []
	matchinglist = []
	for x in range(len(i)):
		if i[x] == "1":
			indexlist.append(int(x))
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

	'''
	One of the final steps, other than writing to a file, I just need to count
	Argueably the most difficult step, need to create a lot of clauses, and test based on the target
	'''
	# Get all the 'counting variables into one list'
	leaflist= []
	for leafs in range(n**3 + 1, varcount + 1):
		# Create the initial list
		leaflist.append(leafs)
	# Create dumy variables to have enough for a perfect binary tree
	dummyleaves = []
	from math import log2
	while log2(len(leaflist))%1 != 0:
		varcount = varcount + 1
		leaflist.append(varcount)
		dummyleaves.append(varcount)
	#Begin making the tree
	countingtree = [leaflist]
	permamount = 2
	for level in countingtree:
		length = len(level)//2
		if length == 0 :
			break # at the top of the tree
		newlevel=[]
		# For each two variables at the current height
		# We make one node above it, with 2hprev-1 permuations
		permamount = (2*permamount)-1
		for _ in range(length):
			templevel=[]
			for x in range(permamount):
				varcount = varcount + 1
				templevel.append(varcount)
			newlevel.append(templevel)
		countingtree.append(newlevel)
	# Lets also put each two leafs into their own list
	tempcounttree = []
	# For each two, put it into a list
	# Want this, b/c it is logically what is beneath the lowest level we have
	for leaf in countingtree[0]:
		tempcounttree.append([leaf])
	countingtree[0] = tempcounttree
	del tempcounttree

	# We have the 'counting tree'
	# Just need to create the logic for it
	# Placed in the counting list
	# We start at h=1
	# Then count the possible variations
	def combos(target, limit):
		#target is the number that we are looking for
		# limit is how high we can go
		combolist=[]
		for lower in range(limit):
			for higher in range(limit):
				if lower + higher == target:
					if lower + higher <= limit:
						combolist.append([lower, higher])
		return combolist


	countinglist = []
	for height, heightlevel in enumerate(countingtree[1:], 1):
		#Heigt is the index, hight level is the current list itself
		#start from slightly above, because we have nothing to imply below that
		prevheight = countingtree[height-1]
		# gives us our place in the tree itself, start at h=1
		for node, nodelevel in enumerate(heightlevel, 0):
			#node level is my current sublist

			#The nodes that we are looking at, a levelbelow
			firstnode = prevheight[2*node]
			secondnode = prevheight[(2*node) + 1]
			for elem, elemlevel in enumerate(nodelevel, 0):
				if height == 1:
					# We know that we're making the comparrison between the leaves
					# and the first level above it. The logic is slightly different, with just two combinations
					if elem == 0:
						#create the and that implies none of the children
						countinglist.append([nodelevel[elem],firstnode[0], secondnode[0]])
					elif elem == 2:
						# create the and that implies all of the children
						countinglist.append([nodelevel[elem], -firstnode[len(firstnode)-1], -secondnode[len(firstnode)-1]])
					else:
						countinglist.append([nodelevel[elem], -firstnode[len(firstnode)-1], secondnode[len(firstnode)-1]])
						countinglist.append([nodelevel[elem], firstnode[len(firstnode)-1], -secondnode[len(firstnode)-1]])
						#otherwise, create the rules that inform of the middle
						#one on, one off, then vice versa
						# May need the and helper for this one
				else:
					## Now we need to count the spot we are at
					if elem == 0:
						#imply the furthest left in the nodes
						countinglist.append([nodelevel[elem],-firstnode[0], -secondnode[0]])
					elif elem == elem:
						#imply the furthest right in the nodes
						countinglist.append([nodelevel[elem], -firstnode[len(firstnode)-1], -secondnode[len(secondnode)-1]])
					else:
						for combo in combos(elemlevel, len(firstnode)): #which one we take the length of does not matter
							countinglist.append([nodelevel[elem], -firstnode[combo[0]], -secondnode[combo[1]]])
						#imply the combinations
						pass

	'''
	Counting variable implies exclusive placement
	'''
	tricklist = []
	def andHelper(firstElem, secondElem,):
		nonlocal varcount
		varcount = varcount + 1
		tricklist.append([firstElem, -varcount])
		tricklist.append([secondElem, -varcount])
		tricklist.append([-firstElem, -secondElem, varcount])
		return varcount
	matchinglist2 = []
	for i in matchinglist:
		#
		matchinglist2.append([andHelper(-i[1],-i[2]),-i[0]])
	'''
	Writing to the file
	'''
	clausenum = len(placementlist) + len(uniquelist) + len(adjacentlist) + len(matchinglist) + len(tricklist) + len(matchinglist2) + len(countinglist) + len(dummyleaves)
	# print(countinglist[len(countinglist)], "\n")
	##varcount is already perfect
	with open(name + ".cnf" , mode ='x') as file:
	#write some basic stuff
		file.write("c for the string {} \n".format(name))
		file.write("p cnf {} {} \n".format(varcount, clausenum))
		#start writing the meat
		for a in placementlist:
			for b in a:
				file.write("{} ".format(b))
			file.write("0 \n")
		for c in uniquelist:
			for d in c:
				file.write("{} ".format(d))
			file.write("0 \n")
		for d in adjacentlist:
			for e in d:
				file.write("{} ".format(e))
			file.write("0 \n")
		for f in matchinglist:
			for g in f:
				file.write("{} ".format(g))
			file.write("0 \n")
		for f in matchinglist2:
			for g in f:
				file.write("{} ".format(g))
			file.write("0 \n")
		for x in countinglist:
			for l in x:
				file.write("{}".format(l))
			file.write("0 \n")
		for x in dummyleaves:
			file.write("-{} ".format(x))
			file.write("0 \n")
		for x in tricklist:
			for y in x:
				file.write("{} ".format(y))
			file.write("0 \n")
		#Done!
if __name__ == "__main__":
	import sys
	protein2sat(sys.argv[1])

def combos(target, limit):
		#target is the number that we are looking for
		# limit is how high we can go
		combolist=[]
		limit = limit + 1
		for lower in range(limit):
			for higher in range(limit):
				if lower + higher == target:
					# if lower + higher <= limit:
					combolist.append([lower, higher])
		return combolist
		# Going to have target + 1 combos if the limit is the length
		# If target is even, should grab (target/2) + 1
		# otherwise, grab 

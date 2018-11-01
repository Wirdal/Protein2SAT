def combos(target, limit):
		#target is the number that we are looking for
		# limit is how high we can go
		combolist=[]
		limit = limit + 1
		for lower in range(limit):
			print(lower)
			for higher in range(limit):
				if lower + higher == target:
					# if lower + higher <= limit:
					combolist.append([lower, higher])
		return combolist
print(combos(4,2))
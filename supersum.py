def super_sum(*args):

	item_sum = 0

	for item in args:
		#Iterate the list if list found
		if type(item) == list:
			for x in range(len(item)):
			# for x in range(0, len(item)):
			# 	if type(x) == int:
			# 		item_sum += x
			# 	elif type(x) == list:
			# 		for j in x:
			# 			item_sum += x[j]
				item_sum += item[x]

		#Cummulate if integer
		elif type(item) == int:
			item_sum += item
		else: 
			return "Item is neither a number or list"
	
	return item_sum

print super_sum(1, 2, 3, 4)
print super_sum([2, 3, 4,5])

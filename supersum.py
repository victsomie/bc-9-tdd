def super_sum(*args):
	'''Add the sum of given integers or items in a list(s) provided
	'''

	item_sum = 0

    #Iterate the args
	for item in args:

		#Check if it is a list and iterate through it
		if type(item) == list:
			for x in item:
				#check if item is an integer there in and add it
				if type(x) == int:
					item_sum += x
				#Check if item is a list inside another list and add items inside
				elif type(x) == list:
					for j in x:
						item_sum += j

		#Cummulate if integer
		elif type(item) == int:
			item_sum += item

		else: 
			return "Item is neither a number or list"
	
	return item_sum

print super_sum(1, 2, 3, 4)
print super_sum(100,200,300)

print super_sum([2, 3, 4, 5, [5,6]], [4,5])
print super_sum([5, 6], [4, 5], 10)

print super_sum([20, 50], [5, 5], [10])
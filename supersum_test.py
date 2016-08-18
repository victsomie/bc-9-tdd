import unittest

from supersum import super_sum

class SuperSumTest(unittest.TestCase):
	"""
	Tests the supersum

	"""
	# def __init__(self):
	# 	#super(ClassName, self).__init__()
	# 	self.arg = arg

	def test_one_number(self):
		self.assertEqual(super_sum(500), 500, msg = "500 should give you 500")

	def  test_one_list(self):
		self.assertEqual(super_sum([2, 5, 8]), 15, msg = "super_sum([2, 5, 8]) should give you 6")

	def test_all_numbers(self):
		self.assertEqual(super_sum(1, 2, 3), 6, msg = "super_sum(1,2,3) should give you 6")
		self.assertEqual(super_sum(100, 200, 300), 600,  msg = "super_sum(100,200,300) should give you 600")

	def test_list_and_numbers(self):
		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30, msg = "Expected sum of items in both lists and numbers")

	def test_all_lists(self):
		self.assertEqual(super_sum([20, 50], [5, 5], [10]), 90, msg = "You should all items in all lists! ")

	def test_string_presence(self):
		self.assertEqual(super_sum([2, "3"]), TypeError, "One item in the list is a string")

if __name__ =='__main__':
	unittest.main()

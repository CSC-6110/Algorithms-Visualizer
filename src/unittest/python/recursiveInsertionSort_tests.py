import unittest
from algorithms.recursiveInsertionSort import recursiveInsertionSort

class RecursiveInsertionSortTest(unittest.TestCase):
	def testCase1(self):
		# Testing with simple 2 element array
		sample_input = [13, 1]
		expected_output = [1,13]
		res = list(recursiveInsertionSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase2(self):
		# Testing with an empty array
		sample_input = []
		expected_output = []
		res = list(recursiveInsertionSort(sample_input))
		self.assertEqual(expected_output, res)

	# def testCase3(self):
	# 	# Testing with odd number of elements
	# 	sample_input = [13, 1, 99]
	# 	expected_output = [([1, 13, 99], 0, 0, 0, 1), ([1, 13, 99], 0, 1, 2, 2)]
	# 	res = list(recursiveInsertionSort(sample_input))
	# 	self.assertEqual(expected_output, res)

	# def testCase4(self):
	# 	# Testing with sorted array
	# 	sample_input = [13, 17]
	# 	expected_output = [([13, 17], 0, 0, 1, 1)]
	# 	res = list(recursiveInsertionSort(sample_input))
	# 	self.assertEqual(expected_output, res)

	# def testCase5(self):
	# 	#Testing with larger numbers
	# 	sample_input = [1904, 264983, 192937, 1357465, 12]
	# 	expected_output = [12, 1904, 192937, 264983, 1357465]
	# 	res = list(recursiveInsertionSort(sample_input))[0][0]
	# 	self.assertEqual(expected_output, res)

	# def testCase6(self):
	# 	# Testing with a longer sorted array
	# 	sample_input = [13, 14, 15, 16, 17]
	# 	expected_output = [13, 14, 15, 16, 17]
	# 	res = list(recursiveInsertionSort(sample_input))[0][0]
	# 	self.assertEqual(expected_output, res)

	# def testCase7(self):
	# 	# Testing with values in descending order
	# 	sample_input = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	# 	expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# 	res = list(recursiveInsertionSort(sample_input))[0][0]
	# 	self.assertEqual(expected_output, res)

	# def testCase9(self):
	# 	# Testing with all zero
	# 	sample_input = [0, 0, 0, 0]
	# 	expected_output = [0, 0, 0, 0]
	# 	res = list(recursiveInsertionSort(sample_input))[0][0]
	# 	self.assertEqual(expected_output, res)



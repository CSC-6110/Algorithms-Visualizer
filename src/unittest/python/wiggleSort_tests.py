import unittest

from algorithms.wiggleSort import wiggleSort


class WiggleSortTest(unittest.TestCase):
    #testCasel - unsorted array 
    def testCasel(self):
        inputArray = [3, 67, 4, 1, 8, 0, 54, 78]
        expectedOutputArray = [3, 67, 1, 8, 0, 54, 4, 78]
        #print ("Input: ", input_array)
        OutputArray = list(wiggleSort(inputArray))[0][0]
        #print ("Output: ", OutputArray)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase2 - empty array     
    def testCase2(self):
        inputArray = []
        expectedOutputArray = []
        #print ("Input: ", input_array)
        OutputArray = list(wiggleSort(inputArray))
        #print ("Output: ", OutputArray)
        self.assertEqual(expectedOutputArray, OutputArray)

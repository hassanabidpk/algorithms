"""
Reference : MIT Algorithms Book
QuickSort(A,p,r)
Algorithm pseudocode

1- if p < r
2-    q = PARTITION(A,p,r)
3-    QuickSort(A,p,q-1)
4-    QuickSort(A,q+1,r)

PARTITION(A,p,r)

1-  x = A[r]
2-  i = p - 1
3-  for j = p to r-1
4-      if A[j]  <= x
5-         i = i + 1
6-         exchange A[i] with A[j]
7-  exchange A[i+1] with A[r]
8-  return i+1

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import unittest

def partition(ar):
	if len(ar) < 2:
		return ar
	pivot = ar[0]
	leftArray = [x for x in ar[1:] if x < pivot]
	rightArray = [x for x in ar[1:] if x >= pivot]
	return (leftArray,pivot,rightArray)

def quicksort(ar):
	if len(ar) < 2:
		return ar
	(l,p,r) = partition(ar)
	result = quicksort(l) + [p] + quicksort(r)
	printresult(result)
	return result

def printresult(ar):
    for a in ar:
        print (a, end=' ')
    print()


class TestQuickSortPartition(unittest.TestCase):
	@classmethod
	def setUp(self):
		print ("start unittest ###")
		self.ar1 = [5,3,4,2,8,1,3]
		self.ar2 = [2,8,7,1,3,5,6,4]
		self.output1 = [3,4,2,1,3,5,8]
		self.output2 = [1, 2, 8, 7, 3, 5, 6, 4]

	def test_partition1(self):
		(l,p,r) = partition(self.ar1)
		r1 = l + [p] + r
		self.assertListEqual(r1,self.output1)

	def test_partition2(self):
		(l,p,r) = partition(self.ar2)
		r2 = l + [p] + r
		self.assertListEqual(r2,self.output2)

	def test_quicksort(self):
		self.result = quicksort(self.ar1)
		self.assertListEqual(self.result,[1,2,3,3,4,5,8])


if __name__ == '__main__':
	unittest.main()

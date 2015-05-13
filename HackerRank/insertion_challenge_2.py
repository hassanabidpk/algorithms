#!/bin/python
"""
In Insertion Sort Part 1, you sorted one element into an array.
 Using the same approach repeatedly, can you sort an entire unsorted array?
"""

def insertionSort(ar):   
	for j in range(1,len(ar)):
		key = ar[j]
		i = j - 1
		while (i >= 0 and ar[i] > key):
			ar[i + 1] = ar[i]
			i = i - 1
			# print ' '.join(map(str, ar))
		ar [i + 1] = key
		print ' '.join(map(str, ar))
	return ar

# m = input()
# ar = [int(i) for i in raw_input().strip().split()]
test_list1 = [1, 4, 3, 5, 6, 2]
insertionSort(test_list1)






#sample output 
# 1 4 3 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 2 3 4 5 6 
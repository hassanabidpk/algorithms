"""
Given a sorted list with an unsorted number V in the rightmost cell, can 
you write some simple code to insert V into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. 
The goal of this challenge is to follow the correct order of insertion sort.
"""

# start implementation 

#!/bin/python
def insertionSort(ar):
    check = len(ar) - 1
    key = ar[len(ar) - 1]
    while (ar[check] >= key and ar[check-1] >= key):
    	ar[check] = ar[check -1]
    	check -=1 
    	print ' '.join(map(str, ar))
    	if(check == 0):
    		break

    ar[check] = key
    print ' '.join(map(str, ar))
    return ar


if __name__ == '__main__':
	test_list1 = [2, 4, 6, 8, 3]
	insertionSort(test_list1)

# output format 
# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8

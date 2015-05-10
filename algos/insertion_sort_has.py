"""
Pseudo code of Insertion Sort 

INSERTION-SORT.A

"""

def insertion_sort(input):

	for j in range(1,len(input)):
		key = input[j]
		i = j - 1
		print "i : ", i , " key : ", key
		while (i >= 0 and input[i] > key):
			input[i + 1] = input[i]
			i = i - 1
			print "intermediate: ", input
		input [i + 1] = key
		print "intermediate: ", input


	return input


list1 = [5, 2, 4, 6, 1, 3,8,1]
list2 = [5,4,3,2,1]
# print (insertion_sort(list1))
print (insertion_sort(list2))

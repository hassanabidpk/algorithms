"""
Reference : MIT Algorithms Book 
QuickSort(A,p,r)
Algorithm pseudocode

1- if p < r
2-    q = PARTITION(A,p,r)
3-    QuickSort(A,p,q-q)
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


def partition(ar):
    pivot = ar[0]
    smallArray = [x for x in ar if x < pivot]
    largeArray = [x for x in ar if x>= pivot]
    printresult(smallArray + largeArray)
def printresult(ar):
    for a in ar:
        print (a, end=' ')
    print


m = input()
ar = [int(i) for i in input().strip().split()]
pivot = ar[0]
partition(ar)
#print (ar)

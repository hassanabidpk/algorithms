from binarytree import BinaryTree
''' Breadth First Search 
	Data Structure Used : Queue (FIFO)
'''

def BreadthFirstSearch(root,fcn):
	queue = [root]
	while len(queue) > 0:
		print ("at node : ",queue[0])
		if fcn(queue[0]):
			return TracePath(queue[0])
		else: 
			temp = queue.pop(0)
		if temp.getLeftBranch():
			queue.append(temp.getLeftBranch())
		if temp.getRightBranch():
			queue.append(temp.getRightBranch())

	return False

# Trace Path 
def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())



def find6(node):
	return node.getValue() == 6
def find10(node):
	return node.getValue() == 10
def find2(node):
	return node.getValue() == 2

#Test 
# Test
n5 = BinaryTree(5)
n2 = BinaryTree(2)
n1 = BinaryTree(1)
n4 = BinaryTree(4)
n8 = BinaryTree(8)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n3 = BinaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)

print ('Depth First Search')
path1 = BreadthFirstSearch(n5, find6)
print([e.getValue() for e in path1])
print ('Depth First Search')
path2 = BreadthFirstSearch(n5, find2)
print([e.getValue() for e in path2])


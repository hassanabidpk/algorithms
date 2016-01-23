from binarytree import BinaryTree
''' Depth First Search 
	Data Structure Used : Stack (LIFO)
'''


def DepthFirstSearch(root,fcn):
	stack = [root]
	result = []
	while len(stack) > 0:
		print ("at node ",str(stack[0].getValue()))
		result.append(stack[0].getValue())
		if fcn(stack[0]):
			print('True --', ",".join(str(x) for x in result))
			# return True
			return TracePath(stack[0])
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0,temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0,temp.getLeftBranch())
	print ('False - Sequence:', ",".join(str(x) for x in result))
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
def findq(node):
	return node.getValue() == "q"

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
n3.setParent(n5)

a = BinaryTree("a")
b = BinaryTree("b")
z = BinaryTree("z")
e = BinaryTree("e")
d = BinaryTree("d")
l = BinaryTree("l")
n = BinaryTree("n")
p = BinaryTree("p")
v = BinaryTree("v")
w = BinaryTree("w")
r = BinaryTree("r")
s = BinaryTree("s")

a.setLeftBranch(b)
a.setRightBranch(p)
b.setParent(a)
p.setParent(a)
b.setRightBranch(z)
p.setRightBranch(v)
z.setLeftBranch(e)
z.setRightBranch(d)
d.setLeftBranch(l)
l.setRightBranch(n)
v.setLeftBranch(w)
v.setRightBranch(r)
r.setLeftBranch(s)
s.setParent(r)
r.setParent(v)
w.setParent(v)
v.setParent(p)
n.setParent(l)
l.setParent(d)
d.setParent(z)
e.setParent(z)
z.setParent(b)


print ('Depth First Search')
path1 = DepthFirstSearch(n5, find6)
# print([e.getValue() for e in path1])
# print ('Depth First Search')
# path2 = DepthFirstSearch(n5, find2)
# print([e.getValue() for e in path2])
# print ('Depth First Search')
# path3 = DepthFirstSearch(a, findq)
# if path3:
# 	print([e.getValue() for e in path3])





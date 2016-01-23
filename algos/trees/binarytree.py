''' 
Binary Tree
'''

class BinaryTree(object):
	def __init__(self,value):
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None 
	# set methods
	def setLeftBranch(self,node):
		self.leftBranch = node
	def setRightBranch(self,node):
		self.rightBranch = node
	def setParent(self,parent):
		self.parent = parent

	# get methods
	def getValue(self):
		return self.value
	def getLeftBranch(self):
		return self.leftBranch
	def getRightBranch(self):
		return self.rightBranch
	def getParent(self):
		return self.parent

	# str method
	def __str__(self):
		return str(self.value)

# Create Binary Tree

if __name__ == '__main__':
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


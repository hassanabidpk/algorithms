'''
This is solution to one of the problems posted on HackerRank
It calculates the height of the Binary Search Tree

Sample Input (first input is number of the nodes in tree)
7 
3
5
2
1
4
6
7

Sample Output
4

'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            cur=Node(data)
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        print(left,right)
        return max(left,right) + 1



if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)
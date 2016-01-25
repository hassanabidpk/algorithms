import sys
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        queue = [root]
        levelOrder = []
        while len(queue) > 0:
            print ("at node : ",queue[0])
            temp = queue.pop(0)
            levelOrder.append(str(temp.data))
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        print (' -> '.join(levelOrder))

if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    myTree.levelOrder(root)


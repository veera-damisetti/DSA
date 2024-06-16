

'''
               5 
          1         2
        2   3    5     6  
      1  2
      
      
IO T   -> 1 2 2 1 3 5 5 2 6 
PreO T -> 5 1 2 1 2 3 2 5 6 
PoO  T -> 1 2 2 3 1 5 6 2 5 
Leaf N -> 1 2 3 5 6 
LevelO -> 5 1 2 2 3 5 6 1 2 
'''
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    
class Tree:
    def __init__(self,root):
        self.root=None
        
    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print(root.data,end=' ')
            self.printInorder(root.right)
        
    def printPreorder(self,root):
        if root:
            print(root.data,end=' ')
            self.printPreorder(root.left)
            self.printPreorder(root.right)
    
    def printPostorder(self,root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.data,end=' ')
    
    def printLeafnodes(self,root):
        if root:
            self.printLeafnodes(root.left)
            if root.left ==None and root.right==None:
                print(root.data,end=' ')
            self.printLeafnodes(root.right)
    
    def printLevelorder(self,root):
        if root is None:
            return None
        q=[]
        q.append(root)
        while len(q)>0:
            print(q[0].data,end=' ')
            node=q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
                
                
    
root=Node(5)
T=Tree(root)
root.left=Node(1)
root.right=Node(2)
root.left.left=Node(2)
root.left.left.left=Node(1)
root.left.left.right=Node(2)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(6)


T.printInorder(root)
print('')
T.printPreorder(root)
print('')
T.printPostorder(root)
print()
T.printLeafnodes(root)
print()
T.printLevelorder(root)



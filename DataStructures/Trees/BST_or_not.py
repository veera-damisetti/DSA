'''
Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Examples:

Input:
   2
 /    \
1      3
        \
         5
Output: true 
Explanation: 
The left subtree of every node contains smaller keys and right subtree of every node contains greater. Hence, the tree is a BST.
Input:
  2
   \
    7
     \
      6
       \
        9
Output: false 
Explanation: 
Since the node with value 7 has right subtree nodes with keys less than 7, this is not a BST. 
Input:
   10
 /    \
5      20
      /   \
     9     25
Output: false
Explanation: The node is present in the right subtree of 10, but it is smaller than 10.
'''

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        def inorder(root,A):
            if root is None:
                return root
            inorder(root.left,A)
            A.append(root.data)
            inorder(root.right,A)
            return A
        
        A=(inorder(root,[]))
        if len(A)!=len(set(A)):
            return False
        if A==sorted(A):
            return True
            
        return False
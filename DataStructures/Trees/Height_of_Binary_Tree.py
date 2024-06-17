'''
Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   
'''


class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        count=0
        # code here
        q=[root]
        A=[root]
        while (len(A)>0 ):
            A=[]
            while len(q)>0:
                temp=q.pop(0)
                if temp.left != None :
                    A.append(temp.left)
                if temp.right !=None :
                    A.append(temp.right)
            q=A.copy()
            count+=1
        return count

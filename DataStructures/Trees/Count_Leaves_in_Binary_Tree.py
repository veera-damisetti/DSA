'''

Given a Binary Tree of size N, You have to count leaves in it. For example, there are two leaves in following tree

        1
     /      \
   10      39
  /
5
'''


def countLeaves(root):
    # Code here
    if root is None: 
        return 0
    if root.left is None and root.right is None:
        return 1 
    return countLeaves(root.left) + countLeaves(root.right)

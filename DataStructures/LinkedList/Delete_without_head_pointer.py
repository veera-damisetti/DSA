'''
You are given a node del_node of a Singly Linked List where you have to delete a value of the given node from the linked list but you are not given the head of the list.

By deleting the node value, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before & after the del_node node should be in the same order.
Note:

Multiple nodes can have the same values as the del_node, but you must only remove the node whose pointer del_node is given to you.
It is guaranteed that there exists a node with a value equal to the del_node value and it will not be the last node of the linked list.
Example 1:

Input:
Linked List = 1 -> 2
del_node = 1
Output: 
2
Explanation: 
After deleting 1 from the linked list, 
we have remaining nodes as 2.
Example 2:

Input:
Linked List = 10 -> 20 -> 4 -> 30
del_node = 20
Output: 
10 4 30
Explanation: 
After deleting 20 from the linked list, 
we have remaining nodes as 10, 4, 30.
'''
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        #code here
        curr=del_node
        curr.data=curr.next.data
        curr=curr.next
        del_node.next=curr.next
        #del del_node
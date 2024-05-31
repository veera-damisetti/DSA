'''
Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 3 
Explanation: 
Middle of linked list is 3.
Example 2: 

Input:
LinkedList: 2->4->6->7->5->1
Output: 7 
Explanation: 
Middle of linked list is 7.
'''

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        curr=head
        len=0
        while curr is not None:
            #print(curr.data)
            curr=curr.next
            len+=1
        curr=head
        l=0
        while curr is not None:
            if l==len//2:
                return curr.data
            l+=1
            curr=curr.next
            
        


# Efficient Approach        
        
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node        
        
        curr1=head
        curr2=head
        while curr2 is not None and curr2.next is not None:
            curr1=curr1.next
            curr2=curr2.next.next
            
        return curr1.data
        
                
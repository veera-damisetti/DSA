'''
Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.

Example 1:

Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output: 8 9 2 4 7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7
Example 2:

Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output: 5 6 7 8 1 2 3 4
'''
# Hint: Rotating -> slicing array 

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        curr=head
        count=0
        while curr:
            count+=1
            if count==k:
                head2=curr.next      
                curr.next=None      #cutting the list
            curr=curr.next
        curr=head2   #starting ar head2 
        if not head2:   # this means no slicing, k= len(list)
            return head
        while curr and curr.next:
            curr=curr.next
        if curr:
            curr.next=head 
        return head2
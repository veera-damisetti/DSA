class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        curr=head
        prev=None
        next=curr.next
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
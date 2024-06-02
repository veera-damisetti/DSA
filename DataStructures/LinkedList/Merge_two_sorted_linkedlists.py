'''

Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
 

Example 1:

Input:
N = 4, M = 3 
valueN[] = {5,10,15,40}
valueM[] = {2,3,20}
Output: 2 3 5 10 15 20 40
Explanation: After merging the two linked
lists, we have merged list as 2, 3, 5,
10, 15, 20, 40.
'''
def sortedMerge(head1, head2):
    # code here
    sorted_head=Node(1)
    s_curr=sorted_head
    curr1=head1
    curr2=head2
    while curr1 and curr2:
        if curr1.data<curr2.data:
            s_curr.next=Node(curr1.data)
            s_curr=s_curr.next
            curr1=curr1.next
        else:
            s_curr.next=Node(curr2.data)
            s_curr=s_curr.next
            curr2=curr2.next
    while curr1:
        s_curr.next=Node(curr1.data)
        s_curr=s_curr.next
        curr1=curr1.next
    while curr2:
        s_curr.next=Node(curr2.data)
        s_curr=s_curr.next
        curr2=curr2.next
    return sorted_head.next
 
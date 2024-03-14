'''
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element
from the unsorted portion of the list and moving it to the sorted portion of the list. 


Time Complexity:  
    Best : O(N^2) 
    Worst : O(N^2) 
Space Complexity: 
    Auxiliary Space: O(1)

'''

A=list(map(int,input().split()))

for i in range(len(A)):
    min_ind = i 
    for j in range(i+1,len(A)):
        if A[min_ind] > A[j]:
            A[j],A[min_ind] = A[min_ind],A[j]
print(A)

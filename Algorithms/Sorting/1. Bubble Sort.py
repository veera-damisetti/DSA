'''
Bubble Sort 

Bubble sort is the simplest sorting algorithm. This also causes it to be quite slow

Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order.


Time Complexity:

Best Case: O(n)
Worst case: O(n^2)

Space Comlexity:

Auxiliary Space: O(1) as no additional space is used.

'''



def bubblesort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                swapped = True
    return A
A=list(map(int,input().split()))
print(bubblesort(A))

'''
Merge Sort is a recursive sorting algorithm.

In Merge Sort, we continuously divide the list into smaller sub-lists. We do this till we reach a sub-list of just 1 element. An list of one element is our base case - an list of 1 element is sorted, and thus we simply return it.

Thus, our recursive case is the one where the list can be divided into further sub list.

Coming back from our base case, we start continuously merging these lists till we get a list  of our original length. 

Time complexity : O(N log(N))   - Best and worst 

'''

A=list(map(int,input().split()))

# Function to merge 2 Sorted arrays in Time Complexity : O(n1 + n2)  , Auxiliary Space : O(n1 + n2)

def merge2sorted(A,B):
    C=[0]*(len(A)+len(B))
    i,j,k=0,0,0
    
    while i < len(A) and j < len(B):
        if A[i] <= B[j] :
            C[k]=A[i]
            k+=1
            i+=1
        else:
            C[k]=B[j]
            j+=1
            k+=1
    
    while i<len(A):
        C[k]=A[i]
        i+=1
        k+=1
        
    while j<len(B):
        C[k]=B[j]
        j+=1
        k+=1
    return C

def mergeSort(A):
    if len(A)==1:
        return A
        
    mid=len(A)//2
    left = A[:mid]
    right = A[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge2sorted(left,right)

print(mergeSort(A))

'''
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 


"Divide and Conquer" strategy

Time Complexity:

 O(log n)

'''
A=list(map(int,input().split()))
key = int(input('Enter the key to search for'))
found = False
low=0
high = len(A)-1
mid = (high + low )//2
while A[mid]!= key and high >= low: 
    mid = (high + low )//2
    if A[mid]==key:
        found = True
        break
    elif A[mid]>key:
        high = mid-1
    else:
        low=mid+1
        
print(found)

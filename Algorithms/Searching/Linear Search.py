'''
Linear Search is defined as a sequential search algorithm
that starts at one end and goes through each element of a list until the desired element is found,
otherwise the search continues till the end of the data set.

Time Complexity: 
Best - O(1)
Worst - O(N)

'''
A=list(map(int,input().split()))
key = int(input('Enter the key to search for'))
found = False
for i in range(len(A)):
    if A[i] == key: 
        print("Found at index:", i)
        found = True
        break
if not found: 
    print("key not found")

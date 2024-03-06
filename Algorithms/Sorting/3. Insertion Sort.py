'''
To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, 
if the key element is smaller than its predecessor, compare it to the elements before. 
Move the greater elements one position up to make space for the swapped element.


Approach / Hints: 
- At every element , check the positioin of that element in left part of the array ( Left part of the array is sorted ) 
- If you find current element less than any of the previous part of the array ,then swap them.
- Current element refers to 'key' in the below code.


Time Complexity: 
  Best: O(N)
  Worst: O(N^2)

Space Complexity:
   O(1) 
   
'''

A=list(map(int,input().split()))

for i in range(1,len(A)):
    key=A[i]
    j=i-1
    while j>=0 and key < A[j]:
        A[j+1]=A[j]
        j -=1
    A[j+1]=key
    print(A)

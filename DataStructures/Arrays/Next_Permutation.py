'''
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.
Examples:

[1,2,3] -> [1,3,2]
[3,2,1] -> [1,2,3]
[1,1,5] -> [1,5,1]
[20, 50, 113] -> [20, 113, 50]

Approch:

1. If all characters are same or the array in descending order, then no answer
2. Traverse from last to first, if you find the descending sequence , then mark that index as start
3. Traverse from last to first, find the first element which is greater than A[start], mark it as end 
4. swap A[end] and A[start]
5. Reverse array from A[start+1] to end 
'''



A=list(map(int,input().split()))

for i in range(len(A)-1,-1,-1):
    if A[i] > A[i-1] :
        start = i-1
        break
for i in range(len(A)-1,-1,-1):
    if A[i] > A[start]:
        end = i
        break
A[end],A[start] = A[start],A[end]
temp= A[start+1:]
temp = temp[::-1]
A[start+1:]=temp

print(A)
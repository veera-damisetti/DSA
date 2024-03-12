'''
Given an integer array arr[], the task is to find the largest sum contiguous subarray of non-negative elements and return its sum.

Examples: 

Input: arr[] = {1, 4, -3, 9, 5, -6} 
Output: 14 
Explanation: 
Subarray [9, 5] is the subarray having maximum sum with all non-negative elements.

Input: arr[] = {12, 0, 10, 3, 11} 
Output: 36 

'''
# Naive Approach

A=list(map(int,input().split()))
sam=[]
start=0
for i in range(len(A)):
    if A[i]<0:
        sam.append(A[start:i])
        start=i+1
sam.append(A[start:])
maxe=0
for element in sam: 
    if sum(element)>maxe:
        maxe = sum(element)
print(maxe)



# Optimal approach
# Traverse the array . if you see non  negative numbers ,  add it to sum and update the max sum . If you see negative number 
# then make sum as 0 and continue

res=0
sum = 0 
for i in range(len(A)):
    if A[i]>=0:
        sum+= A[i]
        res= max(res,sum)
    else:
        sum=0
print(res)



# Approach to print the sub array along with sum 

res=0
a=[]
sum = 0 
temp=[]
for i in range(len(A)):
    if A[i]>=0:
        sum+= A[i]
        temp.append(A[i])
        if sum > res:
            res = sum
            a=temp
    else:
        sum=0
        temp=[]


print(res)
print(a)
        

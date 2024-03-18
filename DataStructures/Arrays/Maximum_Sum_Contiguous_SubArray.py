'''
Maximum Sum Contiguous SubArray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

Example:

Given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.




Kadane's Algorithm

Approach:

- Traverse the array and prepare another array (prefic_sum) which contains sum of arrays so far
- Traverse prefic_sum array and find the answer

In prefic_sum array for every element , find the answer ( curr element - minimum element in left part of array )

'''

A=list(map(int,input().split()))


res=0
min_prefix_sum =0 
prefix_sum =[0]*len(A)
prefix_sum[0]=A[0]
for i in range(1,len(A)):
    prefix_sum[i]=prefix_sum[i-1]+A[i]
    
for i in range(len(A)):
    res= max (res,prefix_sum[i]-min_prefix_sum)
    min_prefix_sum = min(min_prefix_sum,prefix_sum[i])
    
    
print(res)

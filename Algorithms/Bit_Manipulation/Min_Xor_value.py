'''
Given an array of integers of size N find minimum xor of any 2 elements.


Example 1:

Input:
N = 3
arr[] = {9,5,3}
Output: 6
Explanation: 
There are 3 pairs -
9^5 = 12
5^3 = 6
9^3 = 10
Therefore output is 6.

Procedure:
- No need to find every pair
- Xor will be minimum if 2 numbers are close 
- So sort the array and find between adjacent elements

'''

class Solution:
    def minxorpair (self, N, arr):
        # code here 
        arr.sort()
        res=999999999999999
        for i in range(N-1):
            temp=arr[i]^arr[i+1]
            res=min(res,temp)
        return res
        
        
    
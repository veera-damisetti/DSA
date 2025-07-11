'''

Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

Example 1:

Input: 
N = 5, arr[] = {1, 101, 2, 3, 100} 
Output: 
106
Explanation:
The maximum sum of a increasing sequence is obtained from {1, 2, 3, 100},
Example 2:

Input: 
N = 4, arr[] = {4, 1, 2, 3}
Output: 
6
Explanation:
The maximum sum of a increasing sequence is obtained from {1, 2, 3}.
Your Task:  
You don't need to read input or print anything. Complete the function maxSumIS() which takes N and array arr as input parameters and returns the maximum value.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 103
1 ≤ arr[i] ≤ 105
'''

class Solution:
	def maxSumIS(self, Arr, n):
	    '''
		dp=[1]*n
	    sum=Arr.copy()
	    for i in range(1,n):
	        for j in range(i):
	            if Arr[i]>Arr[j]:
	                dp[i]=max(dp[i],dp[j]+1)
	                sum[i]=Arr[i]+sum[j]
	                
	    print(sum)
	    print(max(dp))
	    return max(sum)
		'''
        sum=Arr.copy()
	    for i in range(1,n):
	        for j in range(i):
	            if Arr[i]>Arr[j]:
	                sum[i]=max(Arr[i]+sum[j],sum[i])
	    return max(sum)
	    
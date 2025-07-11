'''
Given a positive integer N, print count of set bits in it. 

Example 1:

Input:
N = 6
Output:
2
Explanation:
Binary representation is '110' 
So the count of the set bit is 2.
Example 2:

Input:
8
Output:
1
Explanation:
Binary representation is '1000' 
So the count of the set bit is 1.
'''
class Solution:
	def setBits(self, N):
		# code here
		count=0
		for i in range(32):
		    mask=1<<i
        if mask&N>0:
		        count+=1
		return count
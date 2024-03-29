'''
Given an array arr[] of n positive integers. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in-place.

Example 1:

Input:
N = 5
Arr[] = {3, 5, 0, 0, 4}
Output: 3 5 4 0 0
Explanation: The non-zero elements
preserve their order while the 0
elements are moved to the right.
Example 2:

Input:
N = 4
Arr[] = {0, 0, 0, 4}
Output: 4 0 0 0
Explanation: 4 is the only non-zero
element and it gets moved to the left.

'''

class Solution:
	def pushZerosToEnd(self,arr, n):
		count=0
		for i in range(n):
			if arr[i]!=0:
				arr[count]=arr[i]
				count +=1
		while count<n:
			arr[count]=0
			count+=1


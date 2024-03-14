'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''


# Naive Approach
'''
if k>len(nums):
            k=len(nums)%k
        for i in range(k):
            nums=[nums[-1]]+nums[:-1]
        print(nums)
'''


# Efficient approach 

def rotate(self, nums: List[int], k: int) -> None:
	def reverse(start, end): # helper method to reverse from start to end
		while start < end: # while there is stuff to reverse
			nums[start], nums[end] = nums[end], nums[start] # swap the elements at the ends
			start, end = start + 1, end - 1 # move pointers closer to each other
			
	n = len(nums)
	k %= n
	reverse(0,n-1) # reverse full list
	reverse(0,k-1) # reverse first k elements (previously the last k elements)
	reverse(k,n-1) # reverse the rest of the list




'''
if you are still confused about how this works, I'll show what nums looks like after each step with the example problems:

Example 1

original nums: [1, 2, 3, 4, 5, 6, 7]
nums after fully reversing: [7, 6, 5, 4, 3, 2, 1]
nums after reversing the first k elements: [5, 6, 7, 4, 3, 2, 1]
nums after reversing the remaining elements: [5, 6, 7, 1, 2, 3, 4]
'''


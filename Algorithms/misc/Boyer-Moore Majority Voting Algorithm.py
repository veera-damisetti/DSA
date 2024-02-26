'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Approach :
The Boyer-Moore voting algorithm is one of the popular optimal algorithms 
which is used to find the majority element among the given elements that have more than N/ 2 occurrences.
This works perfectly fine for finding the majority element which takes 2 traversals over the given elements, 
which works in O(N) time complexity and O(1) space complexity.

Naive Approcah: 

class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        for i in range(n):
            if nums.count(nums[i]) > (n//2):
                return nums[i]
'''



# Best Solution for this is , Boyer-Moore voting algorithm 



  class Solution(object):
    def majorityElement(self, nums):

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate



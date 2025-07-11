'''
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Example 1:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.
Example 2:

Input: 
N = 3
Arr[] = {10, 5, 10}
Output: 5
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5.
Your Task:
You don't need to read input or print anything. Your task is to complete the function print2largest() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. If 2nd largest element doesn't exist then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ N ≤ 105
1 ≤ Arri ≤ 105


'''



class Solution:
    def print2largest(self,arr, n):
        if (n < 2):
            return -1
        first , second = -2147483648,-2147483648
        for i in range(n):
            if (arr[i] > first):
                second = first
                first = arr[i]
            elif (arr[i] > second and arr[i] != first):
                second = arr[i]
        if (second == -2147483648):
            return -1
        else:
            return second
            
            
            
obj=Solution()
A=list(map(int,input().split()))
print(obj.print2largest(A,len(A)))
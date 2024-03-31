'''
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
Explanation: 

Example 2:

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.
Example 3:

Input:
N = 3
arr[] = {6,9,9}
Output:
0
Explanation:
No water will be trapped.
'''


class Solution:
    def trappingWater(self, arr,n):
        
        # Function to find the level of water at a poing in array
        # which will consider left max element and right max element , and minimum of that 2 numbers will be the level 

        def level_finder(A,ind):
            for i in range(len(A)):
                left = max(A[:ind])
                right = max(A[ind+1:])
                
            if left > A[ind] and right > A[ind]:
                return min (left,right)
            return -1  # Means there is no water at that level
        
        S=arr.copy() # to store all the levels 
        for i in range(1,n-1):
            temp = level_finder(arr,i)
            #print(temp)
            if temp == -1:
                pass # Means there is no water at that level
            else:
                S[i]=temp 
                
        res=0
        for i in range(n):
            res+= S[i]-arr[i]
        return res
    
# Few tests were failing with the above approach (Time limit exeeded)

# Efficient Approach

# Storing the current max left and current max right for all elements in one iteration  




class Solution:
    def trappingWater(self, arr,n):
        left_max=[0]*n
        l_m=arr[0]
        r_m=arr[-1]
        right_max=[0]*n
        for i in range(n):
            if arr[i]>=l_m:
                l_m=arr[i]
                left_max[i]=l_m
            else:
                left_max[i]=l_m
                
            i=n-i-1
            if arr[i]>=r_m:
                r_m=arr[i]
                right_max[i]=r_m
            else:
                right_max[i]=r_m
                
                
            
        res=0
        for i in range(1,n-1):
            temp = min(right_max[i],left_max[i])
            res+= temp-arr[i]
        return res
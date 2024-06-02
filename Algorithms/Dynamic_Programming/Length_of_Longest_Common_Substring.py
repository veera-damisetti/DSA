'''
Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.
Example 2:

Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
Output: 1
Explanation: The longest common substrings
are "A", "B", "C" all having length 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommonSubstr() which takes the string S1, string S2 and their length n and m as inputs and returns the length of the longest common substring in S1 and S2.
'''

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        
        A=[[0 for _ in range(n)] for _ in range(m)]
        res=0
        for i in range(m):
            for j in range(n):
                #print(i,j)
                if S1[j]==S2[i]:
                    A[i][j]=A[i-1][j-1]+1
                res=max(res, A[i][j])
        return res
                
                    
       
        
'''
    S1
S2   A B C D G H
  A  1 0 0 0 0 0 
  C  0 0 1 0 0 0 
  D  0 0 0 2 0 0    C D G H 
  G  0 0 0 0 3 0 
  H  0 0 0 0 0 4 
  R  0 0 0 0 0 0 

'''
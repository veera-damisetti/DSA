'''
Given a string S, find the length of the longest substring with all distinct characters. 

Example 1:

Input:
S = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest 
substring with all distinct characters.
Example 2:

Input: 
S = "aaa"
Output: 1
Explanation: "a" is the longest substring 
with all distinct characters.
'''

# Bruteforce Approach 
class Solution:

    def is_distinct(self,s):
        A=[0]*26
        for i in range(len(s)):
            A[ord(s[i])-97]+=1
            if A[ord(s[i])-97]>1:
                return False
            
        return True
    def longestSubstrDistinctChars(self, S):
        # code here
        res=0
        for i in range(len(S)):
            for j in range(i,len(S)):
                if Solution().is_distinct(S[i:j+1]):
                    if len(S[i:j+1])>res:
                        res=len(S[i:j+1])
        return res
     
            


'''

Given string str of length N. The task is to find the minimum characters to be added at the front to make string palindrome.
Note: A palindrome is a word which reads the same backward as forward. Example: "madam".

Example 1:

Input:
S = "abc"
Output: 2
Explanation: 
Add 'b' and 'c' at front of above string to make it
palindrome : "cbabc"
Example 2:

Input:
S = "aacecaaa"
Output: 1
Explanation: Add 'a' at front of above string
to make it palindrome : "aaacecaaa"
Your Task: 
You don't need to read input or print anything. Your task is to complete the function minChar() which takes a string S and returns an integer as output.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= S.length <= 106
'''

class Solution:
    def minChar(self,S):
        '''i=0
        while not Solution().is_palindrome(S):
            #print('db')
            temp=S[len(S)-1-i]
            S=S[0:i]+temp+S[i:]
        
            i+=1
            if i>len(S):
                break
        return i
        '''
        
        '''res=0
        done = 0
        while len(S)>0:
            if Solution().is_palindrome(S):
                done = 1
                break
            else:
                res +=1
                S=S[:-1]
        if done:
            return res
            '''
            
        start=0
        end = len(S)-1
        res=0
        while start<end:
            if S[start]==S[end]:
                start+=1
                end-=1
            else:
                start=0
                res+=1
                end = len(S)-res-1
            
        return res
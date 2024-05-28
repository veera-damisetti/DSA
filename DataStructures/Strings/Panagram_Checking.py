'''
Given a string s check if it is "Panagram" or not.

A "Panagram" is a sentence containing every letter in the English Alphabet.

Example 1:

Input:
s = "Bawds jog, flick quartz, vex nymph"
Output: 
1
Explanation: 
In the given input, there
are all the letters of the English
alphabet. Hence, the output is 1.
'''

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        if len(s)<26:
            return 0
        A=[0]*26
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalpha():
                A[97-ord(s[i])]+=1
        if 0 in A: 
            return 0
        return 1
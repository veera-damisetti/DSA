'''
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number. 

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)

Constraints:
1<=roman no range<=3999

'''
class Solution:
    def romanToDecimal(self, S): 
        # code here
        
        res=0
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }

        for i in range(len(S)-1):
            if val[S[i]]<val[S[i+1]]:
                res-=val[S[i]]
            else:
                res+=val[S[i]]
        res+=val[S[-1]]       # As last element always will be added to result 
        return res
    

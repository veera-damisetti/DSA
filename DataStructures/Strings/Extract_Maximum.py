'''
Given a alphanumeric string S, extract maximum numeric value from S.

Example 1:

Input:
S = 100klh564abc365bg
Output: 564
Explanation: Maximum numeric value 
among 100, 564 and 365 is 564.
Example 2:

Input:
S = abcdefg
Output: -1
Explanation: Return -1 if no numeric 
value is present. 

Your Task:  
You dont need to read input or print anything. Complete the function extractMaximum() which takes the string S as input parameters and returns the maximum numeric value. If it is not present in S, return -1.

 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

'''
class Solution:
    def extractMaximum(self,S): 
        # code here
        res=-1
        temp=''
        for i in range(len(S)):
            if S[i].isdigit():
                temp+=S[i]
                if int(temp)>res:
                    res=int(temp)
            else:
                temp=''
        return res

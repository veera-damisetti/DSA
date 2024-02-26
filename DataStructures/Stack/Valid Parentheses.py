'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        St=[]
        for i in range(len(s)):
            if s[i] in '[{(':
                St.append(s[i])
            else:
                if len(St)==0:
                    return False
                if s[i]== ')':
                    if St[-1]=='(':
                        St=St[:-1]
                    else:
                        return False
                elif s[i]=='}':
                    if St[-1]=='{':
                        St=St[:-1]
                    else:
                        return False
                elif s[i]==']':
                    if St[-1]=='[':
                        St=St[:-1]
                    else:
                        return False

        if len(St)>0:        # If stack has some chars leftover , this means parentheses are not balanced
            return False
        return True
      

# Calling the method

a=input('Enter string ')      
x=Solution()
print(x.isValid(a))


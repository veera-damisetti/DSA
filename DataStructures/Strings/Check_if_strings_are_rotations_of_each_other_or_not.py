'''
You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase.

Example 1:

Input:
geeksforgeeks
forgeeksgeeks
Output: 
1
Explanation: s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.
Example 2:

Input:
mightandmagic
andmagicmigth
Output: 
0
Explanation: Here with any amount of
rotation s2 can't be obtained by s1.
Your Task:
You don't have to read or print anything. The task is to complete the function areRotations() which takes two strings, s1 and s2 as inputs and checks if the two strings are rotations of each other. The function returns true if s1 can be obtained by rotating s2, else it returns false.

Expected Time Complexity: O( |s1| ).
Expected Space Complexity: O( |s1| ).

Constraints:
1 <= |s1|, |s2| <= 105
'''


# Naive approach ( Use queue )
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        for i in range(len(s1)):
            s1=s1[1:]+s1[0]       # Here use double ended queue
            if s1==s2:
                return 1
            
        return 0
    



# Efficient Approcah

'''
Efficient Approach: Follow the given steps to solve the problem

Create a temp string and store concatenation of str1 to str1 in temp, i.e temp = str1.str1
If str2 is a substring of temp then str1 and str2 are rotations of each other.


Works for arrays also 
'''
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        temp=s1+s1
        if s2 in temp:
            return 1
        return 0
    


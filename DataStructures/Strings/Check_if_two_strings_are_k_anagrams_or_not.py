'''
Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.

Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.

Example:

Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the given function areKAnagrams that returns true if the strings can be turned into K-anagrams, else return false.

Constraints:
1 ≤ length of String ≤ 105
1 ≤ K ≤ length of String



Here we use only one count array to store counts of characters in str1.
We traverse str2 and decrement occurrence of every character in count array that is present in str2. 
If we find a character that is not there in str1, we increment count of different characters. 
If count of different character become more than k, we return false.
'''

class Solution:
    def areKAnagrams(self, str1, str2, k):
        # code here
        if len(str1)!=len(str2):
            return False
        A=[0]*26
        for i in range(len(str1)):
            A[ord(str1[i])-97]+=1 # 97 is ASCII of 'a'
            
        count = 0 
        for i in range(len(str1)):
            if A[ord(str2[i])-97]>0:
                 A[ord(str2[i])-97] -= 1
            else:
                count +=1
                
            if count>k:
                return False
                
        return True
        
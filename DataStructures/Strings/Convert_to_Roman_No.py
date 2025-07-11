'''
Given an integer n, your task is to complete the function convertToRoman which prints the corresponding roman number of n. Various symbols and their values are given below
Note:- There are a few exceptions for some numbers like 4 in roman is IV,9 in roman is IX, similarly, 40 is XL while 90 is XC. Similarly, 400 is CD while 900 is CM

I 1
V 5
X 10
L 50
C 100
D 500
M 1000

 

Example 1:

Input:
n = 5
Output: V
 

Example 2:

Input:
n = 3
Output: III
 

Your Task:
Complete the function convertToRoman() which takes an integer N as input parameter and returns the equivalent roman. 

 

Expected Time Complexity: O(log10N)
Expected Auxiliary Space: O(log10N * 10)

 

Constraints:
1<=n<=3999
'''


class Solution:
    def convertRoman(self, n):
        #Code here
        num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        res=''
        
        while n:
            div = n//num[i]
            n=n%num[i]
            while div:
                res+=sym[i]
                div-=1
            i+=1
            
        return res
    
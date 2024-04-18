'''
Given a decimal number m. Convert it into a binary string and apply n iterations, in each iteration 0 becomes 01, and 1 becomes 10. Find the kth (1-indexing) character in the string after the nth iteration.

Example 1:

Input: m = 5, n = 2, k = 5
output: 0
Explanation: Binary representation of m 
is "101", after one iteration binary 
representation will be "100110", and after 
second iteration binary representation 
will be "100101101001". 
Example 1:

Input: m = 5, n = 2, k = 1
output: 1
Explanation: Binary representation of m 
is "101", after one iteration binary 
representation will be "100110", and after 
second iteration binary representation
will be "100101101001". 
Your task:
You do not need to read any input or print anything. The task is to complete the function kthCharacter(), which takes 3 integers m, n, and k as input and returns a character.

Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n)
'''


'''
class Solution:
    
    def decimal_to_binary(self,decimal_num):
        binary_str = format(int(decimal_num), 'b')
        return binary_str
    
	def kthCharacter(self, m, n, k):
		# code here
		b=Solution().decimal_to_binary(m)
		
		for i in range(n):
		    temp=''
		    for i in range(len(b)):
		        if b[i]=='0':
		            temp+='01'
		        else:
		            temp+='10'
		            
		    b=temp
		return b[k-1]

        '''
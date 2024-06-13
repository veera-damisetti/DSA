'''
Given a number n, find the nth number in the Padovan Sequence.

A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1

Note: Since the output may be too large, compute the answer modulo 10^9+7.

Examples :

Input: n = 3
Output: 2
Explanation: We already know, P1 + P0 = P3 and P1 = 1 and P0 = 1
Input: n = 4
Output: 2
Explanation: We already know, P4  = P2 + P1 and P2 = 1 and P1 = 1
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
'''

class Solution:
    def padovanSequence(self, n):
        # code here 
        '''
        mod=pow(10,9)+7
        if n<=2:
            return 1
        A=[0]*(n+1)
        A[0],A[1],A[2]=1,1,1
        
        for i in range(3,n+1):
            A[i]=(A[i-2]+A[i-3])%mod
        #print(A)
        return A[n]%mod
        '''
        
        MOD = 10**9 + 7
    
    
        if n == 0 or n == 1 or n == 2:
            return 1
    
    
        p0, p1, p2 = 1, 1, 1
    
    
        for i in range(3, n + 1):
            p_next = (p1 + p0) % MOD
            p0, p1, p2 = p1, p2, p_next
    
        return p2

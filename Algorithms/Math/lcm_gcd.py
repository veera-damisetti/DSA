class Solution:
    def lcmAndGcd(self, A , B):
        # code here
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        lcm=(A/gcd(A,B))*B
        gcd=gcd(A,B)
        return [int(lcm),int(gcd)]
            

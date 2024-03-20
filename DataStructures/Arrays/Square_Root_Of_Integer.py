'''
Implement int sqrt(int x).

Compute and return the square root of x.

*** If x is not a perfect square, return floor(sqrt(x)) ***

Example:

Input : 11
Output : 3
Warning: DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY




Binary Search

'''

def sqrt(n):
    low = 0 
    high = n//2
    mid = (high + low)//2
    res=0
    while high >= low:
        if mid*mid == n:
            return mid
        elif mid*mid > n:
            high = mid-1
        else:
            low=mid+1
            res=max(res,mid)
        mid = (high+low)//2
    return res
        
    
    
print(sqrt(int(input('Enter integer'))))
    

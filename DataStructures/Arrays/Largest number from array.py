'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

'''

A=list(map(int,input().split()))
def comp(A,B):
    A=str(A)
    B=str(B)
    num1= int(A+B)
    num2= int(B+A)
    if num1 > num2 :
        return -1
    return 1

import functools
A=sorted(A,key=functools.cmp_to_key(comp))

for i in range(len(A)):
    print(str(A[i]),end='')

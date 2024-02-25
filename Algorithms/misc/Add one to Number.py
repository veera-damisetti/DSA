'''
You are given a non-negative number represented as an array of digits.

Example: 123 is represented as [1,2,3]

You must add 1 to the number ( increment the number represented by the digits ) and return the required array or list.

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3], the returned vector should be [1, 2, 4],

as 123 + 1 = 124.

Some notes:

Your returned array must not have any leading zeros. Example:
Input:
[0,0,2,1]
 
Ouput:
[2,2] // no leading zeros
Maximum size of the array is 300 so avoid converting it to a string or an integer. Instead, try to think of what happens when 1 is added to the number.


 

Approach: 

- Start traversing the array from Reverse and assume a variable 'carry'  as 1 which we need to add to the number
- if A[i] is 9 and carry is 1 , that means we need to have a 0 there and still need to carry 1 
- if not equals to 9 , simply add 1 the element and make carry 0 as we are done
- Check at the last of carry is still 1, as this means we have all 9s in the array 
- Remove leading zeros

 
'''

def plusOne(A):
    i=len(A)-1
    carry = 1
    while i>=0:
        if A[i]==9 and carry ==1:
            A[i]=0
        else:
            A[i]=A[i]+carry
            carry=0
        i-=1
        
    if carry==1:    # Handling corner case of all 9s
        A=[1]+A
    while A[0]==0:   #Removing leading zeroes
        A=A[1:]
    
    return A

A=list(map(int,input().split()))   # Reading a list from user , as space separated integers
print(plusOne(A))

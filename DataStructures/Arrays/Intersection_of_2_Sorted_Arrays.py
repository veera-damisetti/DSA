'''
Intersection of 2 Sorted Arrays
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input Format
The first line contains T, the number of test cases. Following T lines contain:
Line 1 contains N1, followed by N1 integers of the first array
Line 2 contains N2, followed by N2 integers of the second array
Output Format
The intersection of the arrays in a single line

Example
Input:
1
3 10 17 57
6 2 7 10 15 57 246

Output:

10 57

Input:
1
6 1 2 3 3 4 5 6
2 1 6

Output:
1 6


2 Pointer algorithm
'''
A = list(map(int,input("Enter Array A").split()))
B = list(map(int,input("Enter Array B").split()))

i = 0
j = 0
while i<len(A) and j < len(B):
    if A[i]==B[j]:
        print(A[i])
    if A[i]>B[j]:
        j+=1
    else:
        i+=1



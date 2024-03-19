'''
Queried Operations
Given an Array A, with n elements and also a set of Q queries.

Each query contains L and R and V. Your task is to add V for all indexes from L to R, both inclusive.

Finally, print the array after all Q queries.

Constraints

1 <= N <= 106
1 <= Q <= 106
1 <= L, R, <= N
Input format

First line contains N, followed by N elements of the array
Next line contains Q, the number of queries
This is followed by Q lines, each containing the respective L, R and V
Output format

Print the array in a single line after all queries are completed.



Approach using prefix sum concept:
- create an array of size len(A)
- for each query L R V , update ps[L] = V and ps[R]= -V
- Caluculate the prefix sum array for the array ps 
- Then add corresponding elements of A and ps 

'''


A=list(map(int,input().split()))
n=int(int(input()))
Q=[]
for i in range(n):
    Q.append(list(map(int,input().split())))



ps=[0]*(len(A))
for i in range(len(Q)):
    
    ps[Q[i][0]] += Q[i][-1]
    if Q[i][1]+1 < len(A):
        ps[Q[i][1]+1] += -Q[i][-1]
    
for i in range(1,len(ps)):
    ps[i]=ps[i]+ps[i-1]
 
 
 
print()   
for i in range(len(A)):
    print(A[i]+ps[i],end=' ')


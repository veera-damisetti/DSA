'''
Anti Diagonals
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

Input:

1 2 3
4 5 6
7 8 9
Return:

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
Input:

1 2
3 4
Return:

[
  [1],
  [2, 3],
  [4]
]



Hint: 
Observe the pattern of indeces , in all anti-diagonals , sum of the indeces i and j is equal 

00 01 02
10 11 12
20 21 22


'''





# Naive approach
n=int(input('Enter number of rows\n'))
A=[]
res=[]
for i in range(n):
    A.append(list(map(int,input().split())))
    
for x in range((2*n)-1):
    temp=[]
    for i in range(n):
        for j in range(n):
            if i+j == x:
                temp.append(A[i][j])
    res.append(temp)
        
    
for row in res: 
    print(row)



# Efficient approach

n=int(input('Enter number of rows\n'))
A=[]
res=[]
for i in range(n):
    A.append(list(map(int,input().split())))
    
for i in range(2*n-1):
    res.append([])

for i in range(n):
    for j in range(n):
        res[i+j].append(A[i][j])
for row in res:
    print(row)




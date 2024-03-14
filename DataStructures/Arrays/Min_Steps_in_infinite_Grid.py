'''
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x-1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [1, 1] [ 1, 2]
Output : 1
It takes one  step to move from (1, 1) to (1, 2).

'''


A=list(map(int,input().split()))
B=list(map(int,input().split()))

x1,y1=A[0],A[1]
x2,y2=B[0],B[1]

print (max(abs(x2-x1),abs(y2-y1)))

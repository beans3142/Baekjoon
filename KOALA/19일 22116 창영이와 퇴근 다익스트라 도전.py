from sys import stdin
from heapq import *

input=stdin.readline
dx,dy=[0,0,1,-1],[1,-1,0,0]

n=int(input())
load=[list(map(int,input().split())) for i in range(n)]
value_table=[[-1 for i in range(n)]for j in range(n)]

v=[[0,0,0]]

while True:
    lean,x,y=heappop(v)
    if value_table[y][x]!=-1:
        continue
    if y==n-1 and x==n-1:
        print(lean)
        break
    value_table[y][x]=lean
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if value_table[ny][nx]!=-1:
                continue
            heappush(v,[max(abs(load[y][x]-load[ny][nx]),lean),nx,ny])
'''
from sys import stdin
from collections import deque
from heapq import *
from math import inf
input=stdin.readline
dx,dy=[0,0,1,-1],[1,-1,0,0]


n=int(input())
load=[list(map(int,input().split())) for i in range(n)]
value_table=[[inf for i in range(n)]for j in range(n)]
mn=inf

v=[[0,load[0][0],0,0]]

while v:
    total,height,x,y=heappop(v)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            gyungsa=0 if height>load[ny][nx] else load[ny][nx]-height
            if value_table[ny][nx]>total+gyungsa:
                value_table[ny][nx]=total+gyungsa
                heappush(v,[total+gyungsa,load[ny][nx],nx,ny])
    
print(value_table[-1][-1] if value_table[-1][-1] != inf else 0)
'''


"""
--------
5
5 9 4 4 4
4 9 4 9 4
4 9 4 9 4
4 9 4 9 4
4 4 4 9 4

답 1
--------
3
3 4 1
9 1 8
9 9 9

답 6
---------
3
3 4 1
9 7 8
8 9 9

답 3
----------
6
2 1 2 2 2 2
2 1 2 1 2 2
2 1 2 1 2 2
2 1 2 1 2 2
2 1 2 1 2 2
2 2 2 1 2 2

답 0
-----------
5
4 5 8 7 2
8 6 2 10 9
3 4 15 6 20
4 9 4 3 2
3 2 3 5 1

답 5
-----------
1
아무 숫자

답 0
-----------
3
9 9 9
9 9 9
9 1 3

답 6
---------
5
1 14 15 16 17
2 13 12 19 18
3 10 11 20 21
4 9 8 23 22
5 6 7 24 25
답 1
"""

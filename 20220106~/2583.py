from sys import *
from collections import *
#from math import *
#from itertools import *
#from heapq import *
#from bisect import *
#setrecursionlimit(100000)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
input=stdin.readline

n,m,k=map(int,input().split())
board=[[0 for i in range(m)] for j in range(n)]

for _ in range(k):
    sx,sy,ex,ey=map(int,input().split())
    for i in range(sy,ey):
        for j in range(sx,ex):
            board[i][j]=1

def bfs(X,Y):
    queue=deque([(X,Y)])
    board[Y][X]=1
    size=0
    while queue:
        x,y=queue.popleft()
        size+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if board[ny][nx]==0:
                    board[ny][nx]=1
                    queue.append((nx,ny))
    return size
    
ans=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            ans.append(bfs(j,i))

print(len(ans))
print(*sorted(ans))

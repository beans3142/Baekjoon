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

l,w=map(int,input().split())
arr=[input().rstrip() for i in range(l)]

def bfs(X,Y):
    
    vi=[[0 for i in range(w)] for j in range(l)]
    
    queue=deque([(X,Y)])
    vi[Y][X]=1
    move=0
    
    while queue:
        moved=False
        le=len(queue)
        for i in range(le):
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if -1<nx<w and -1<ny<l:
                    if vi[ny][nx]==0 and arr[ny][nx]=='L':
                        moved=True
                        vi[ny][nx]=1
                        queue.append((nx,ny))
        if moved==False:
            break
        move+=1
    return move
                
ans=0

for i in range(l):
    for j in range(w):
        if arr[i][j]=='L':
            ans=max(ans,bfs(j,i))

print(ans)

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
n,m=map(lambda x:int(x)+2,input().split())
matrix=[[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for i in range(n-2)]+[[0]*(m+2)]
vi=[[0 for i in range(m+2)] for i in range(n+2)]
time=0
ans=0

while True:
    melt=False
    queue=deque([(0,0)])
    nextmelt=[]
    vi[0][0]=time+1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]<time+1:
                    if matrix[ny][nx]==1:
                        nextmelt.append((nx,ny))
                    else:
                        queue.append((nx,ny))
                    vi[ny][nx]=time+1
    if nextmelt:
        melt=True
        time+=1
        ans=len(nextmelt)
        for meltx,melty in nextmelt:
            matrix[melty][meltx]=0
    else:
        break

print(time)
print(ans)
    

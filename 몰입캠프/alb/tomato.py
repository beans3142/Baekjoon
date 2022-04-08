from sys import *
from collections import *
#from math import *
#from itertools import *
#from heapq import *
#from bisect import *
#setrecursionlimit(100000)
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
input=stdin.readline

m,n,h=map(int,input().split())
arr=[[list(map(int,input().split())) for i in range(n)] for j in range(h)]
vi=[[[0 for i in range(m)] for j in range(n)] for k in range(h)]
left=0
queue=deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==0:
                left+=1
            elif arr[i][j][k]==1:
                queue.append((k,j,i))
                vi[i][j][k]=1

day=0
if left==0:
    print(0)
    exit()
while queue:
    le=len(queue)
    if left==0:
        break
    for i in range(le):
        x,y,z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if -1<nx<m and -1<ny<n and -1<nz<h:
                if arr[nz][ny][nx]==0:
                    arr[nz][ny][nx]=1
                    left-=1
                    queue.append((nx,ny,nz))

    day+=1

if left==0:
    print(day)
else:
    print(-1)

    

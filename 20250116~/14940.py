from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            x=j
            y=i
vi=[[0]*m for i in range(n)]
vi[y][x]=0
q=deque([(x,y)])
while q:
    x,y=q.popleft()
    for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if -1<ny<n and -1<nx<m:
            if vi[ny][nx]==0 and arr[ny][nx]==1:
                vi[ny][nx]=vi[y][x]+1
                q.append((nx,ny))
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 or arr[i][j]==2:
            print(0,end=' ')
        elif vi[i][j]:
            print(vi[i][j],end=' ')
        else:
            print(-1,end=' ')
    print()

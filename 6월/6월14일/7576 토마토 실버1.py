import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())

mato=[list(map(int,input().split())) for i in range(n)]
visited=[[[0,0] for i in range(m)]for i in range(n)]
arr=[]
dx,dy=[1,-1,0,0],[0,0,1,-1]
mato_left=0
min_day=0

def bfs(arr):
    make_mato=0
    queue=deque(arr)
    while queue:
        x,y,t=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<m:
                if visited[nx][ny][0]==0 and mato[nx][ny]==0:
                    visited[nx][ny][0]=1
                    visited[nx][ny][1]=t
                    queue.append([nx,ny,t+1])
                    make_mato+=1
    return make_mato

for i in range(n):
    for j in range(m):
        if mato[i][j]==0:
            mato_left+=1
        elif mato[i][j]==1:
            arr.append([i,j,1])

mato_left-=bfs(arr)

if mato_left==0:
    for i in range(n):
        for j in range(m):
            min_day=max(visited[i][j][1],min_day)
    print(min_day)
else:
    print(-1)

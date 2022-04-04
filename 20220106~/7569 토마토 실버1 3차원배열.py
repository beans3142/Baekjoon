import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())

mato=[[list(map(int,input().split())) for i in range(n)]for _ in range(h)]
visited=[[[[0,0] for i in range(m)]for i in range(n)]for i in range(h)]
arr=[]
dx,dy,dz=[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
mato_left=0
min_day=0

def bfs(arr):
    make_mato=0
    queue=deque(arr)
    while queue:
        z,x,y,t=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h:
                if visited[nz][nx][ny][0]==0 and mato[nz][nx][ny]==0:
                    visited[nz][nx][ny][0]=1
                    visited[nz][nx][ny][1]=t
                    queue.append([nz,nx,ny,t+1])
                    make_mato+=1
    return make_mato
for l in range(h):
    for i in range(n):
        for j in range(m):
            if mato[l][i][j]==0:
                mato_left+=1
            elif mato[l][i][j]==1:
                arr.append([l,i,j,1])

mato_left-=bfs(arr)

if mato_left==0:
    for l in range(h):
        for i in range(n):
            for j in range(m):
                min_day=max(visited[l][i][j][1],min_day)
    print(min_day)
else:
    print(-1)

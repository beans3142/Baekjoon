from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1,1,1,2,2,-2,-2,-1,-1]
dy=[1,-1,0,0,2,-2,1,-1,-1,1,2,-2]

k=int(input())
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]

vi=[[[-1]*m for _ in range(n)] for _ in range(k+1)]

queue=deque([(0,0,0)])
vi[0][0][0]=0

while queue:
    x,y,use=queue.popleft()
    for i in range(12):
        nx=x+dx[i]
        ny=y+dy[i]
        nuse=use+(i>3)
        if nuse<=k and -1<nx<m and -1<ny<n:
            if arr[ny][nx]==0 and vi[nuse][ny][nx]==-1:
                vi[nuse][ny][nx]=vi[use][y][x]+1
                queue.append((nx,ny,nuse))

ans=1e10
for i in range(k+1):
    ans=min(ans,vi[i][-1][-1] if vi[i][-1][-1]!=-1 else 1e10)
print(ans if ans!=1e10 else -1)
        

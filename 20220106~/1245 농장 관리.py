from sys import stdin
input=stdin.readline
from collections import deque
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(m)]
v=[[0 for i in range(n)] for i in range(m)]
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,-1,1,-1,1]

def bfs(X,Y):
    global arr
    queue=deque([[X,Y]])
    able=True
    h=arr[Y][X]
    v[Y][X]=1
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<m:
                if h==arr[ny][nx] and v[ny][nx]!=1:
                    v[ny][nx]=1
                    queue.append([nx,ny])
                elif h<arr[ny][nx]:
                    able=False
    if able:
        return 1
    return 0

cnt=0
for i in range(m):
    for j in range(n):
        if v[i][j]!=1:
            cnt+=bfs(j,i)

print(cnt)

from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

maze=[list(map(int,input().split())) for i in range(n)]
vi=[[0 for i in range(m)] for i in range(n)]

queue=deque([(0,n-1)])
vi[n-1][0]=1

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<m and -1<ny<n:
            if maze[ny][nx]==0 and vi[ny][nx]==0:
                vi[ny][nx]=vi[y][x]+1
                queue.append((nx,ny))

print(vi[0][m-1]-1)

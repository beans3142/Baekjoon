from sys import stdin
from collections import *
input=stdin.readline

inf=float('inf')

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

hy,hx=map(lambda x: int(x)-1,input().split())
ey,ex=map(lambda x: int(x)-1,input().split())

arr=[list(map(int,input().split())) for i in range(n)]
dist=[[[inf,inf] for i in range(m)] for j in range(n)]

queue=deque([(hx,hy,0)])
dist[hy][hx][0]=0
ans=-1

while queue:
    x,y,isBreak=queue.popleft()
    if x==ex and y==ey:
        print(dist[ey][ex][isBreak])
        exit()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<m and -1<ny<n:
            if arr[ny][nx]==0:
                if dist[ny][nx][isBreak]==inf or dist[ny][nx][isBreak]>dist[y][x][isBreak]+1:
                    dist[ny][nx][isBreak]=dist[y][x][isBreak]+1
                    queue.append((nx,ny,isBreak))
            elif isBreak==0:
                dist[ny][nx][1]=dist[y][x][0]+1
                queue.append((nx,ny,1))

print(-1)

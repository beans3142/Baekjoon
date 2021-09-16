import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
rgb=[input().rstrip() for i in range(n)]
rg_b=[[0 for i in range(n)]for i in range(n)]
visited=[[0 for i in range(n)]for i in range(n)]
rgb_value={'R':1,'G':1,'B':0}
dx,dy=[0,0,1,-1],[1,-1,0,0]
cnt=0
sakyak_cnt=0

def bfs_normal(X,Y):
    queue=deque()
    queue.append([X,Y])
    visited[Y][X]=1
    rg_b[Y][X]=rgb_value[rgb[Y][X]]
    while queue:
        x,y=queue.popleft()
        nowblock=rgb[y][x]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if nowblock==rgb[ny][nx] and visited[ny][nx]==0:
                    queue.append([nx,ny])
                    visited[ny][nx]=1
                    rg_b[ny][nx]=rgb_value[rgb[ny][nx]]
                    
def bfs_sakyak(X,Y):
    queue=deque()
    queue.append([X,Y])
    visited[Y][X]=0
    while queue:
        x,y=queue.popleft()
        nowblock=rg_b[y][x]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if nowblock==rg_b[ny][nx] and visited[ny][nx]==1:
                    queue.append([nx,ny])
                    visited[ny][nx]=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs_normal(j,i)
            cnt+=1

for i in range(n):
    for j in range(n):
        if visited[i][j]==1:
            bfs_sakyak(j,i)
            sakyak_cnt+=1

print(cnt,sakyak_cnt)

from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]=='2': q.append((j,i))
vi=[[-1]*m for i in range(n)]
vi[q[0][1]][q[0][0]]=0
while q:
    x,y=q.popleft()
    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx=x+dx
        ny=y+dy
        if -1<nx<m and -1<ny<n:
            if vi[ny][nx]==-1 and arr[ny][nx]!='1':
                if arr[ny][nx]!='0':
                    print("TAK")
                    print(vi[y][x]+1)
                    exit()
                vi[ny][nx]=vi[y][x]+1
                q.append((nx,ny))
print("NIE")

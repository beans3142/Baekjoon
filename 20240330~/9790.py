from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    
    vi=[[0]*m for i in range(n)]
    queue=deque([(x,y)])
    vi[y][x]=1
    cnt=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]==0 and arr[ny][nx]=='.':
                    vi[ny][nx]=1
                    queue.append((nx,ny))
                    cnt+=1
    return cnt


while True:
    m,n=map(int,input().split())
    if n==m==0:
        break
    arr=[input().rstrip() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]=='A':
                print(bfs(j,i))
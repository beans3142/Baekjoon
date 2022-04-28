from sys import stdin
from collections import deque
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,-1,1]

n,m,k=map(int,input().split())
matrix=[list(map(int,list(input().rstrip()))) for i in range(n)]
vi=[[[0 for i in range(m)]for j in range(n)] for k in range(k+1)]

def bfs():
    queue=deque([(0,0,0)]) # x, y 벽 부숨 여부
    vi[0][0][0]=1
    while queue:
        x,y,useAxe=queue.popleft()
        if x==m-1 and y==n-1:
            return vi[useAxe][y][x]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[useAxe][ny][nx]==0:
                    if matrix[ny][nx] and useAxe<k and not vi[useAxe+1][ny][nx]:
                        vi[useAxe+1][ny][nx]=vi[useAxe][y][x]+1
                        queue.append((nx,ny,useAxe+1))
                    elif matrix[ny][nx]==0:
                        vi[useAxe][ny][nx]=vi[useAxe][y][x]+1
                        queue.append((nx,ny,useAxe))
    return -1

print(bfs())

from sys import stdin
from collections import deque
input=stdin.readline

inf=float('inf')

dx=[1,-1,0,0]
dy=[0,0,-1,1]

n,m,k=map(int,input().split())
matrix=[list(map(int,list(input().rstrip()))) for i in range(n)]
vi=[[[[0 for i in range(m)]for i in range(n)]\
     for i in range(k+1)] for i in range(2)]

def bfs():
    queue=deque([(0,0,0,False)]) # x, y 벽 부숨 여부
    vi[0][0][0][0]=1
    ans=inf
    while queue:
        x,y,useAxe,time=queue.popleft()
        if x==m-1 and y==n-1:
            return vi[useAxe][y][x]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[not time][useAxe][ny][nx]==0:
                    if matrix[ny][nx] and useAxe<k \
                       and vi[not time][useAxe+1][ny][nx]:
                        if time:
                            vi[not time][useAxe][ny][nx]=vi[time][useAxe][y][x]+1
                            queue.append((nx,ny,useAxe,not time))
                        else:
                            vi[not time][useAxe+1][ny][nx]=vi[time][useAxe][y][x]+1
                            queue.append((nx,ny,useAxe+1,not time))
                    elif matrix[ny][nx]==0:
                        vi[not time][useAxe][ny][nx]=vi[time][useAxe][y][x]+1
                        queue.append((nx,ny,useAxe,not time))
    return -1

print(bfs())


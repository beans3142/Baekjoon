#https://www.acmicpc.net/problem/2178
'''
import sys
from collections import *

input=sys.stdin.readline

n,m=map(int,input().split())
#n,m=4,6
maze=[input()[:-1] for i in range(n)]
maze=[[0]*(m+2)]+[[0]+list(i)+[0]for i in maze]+[[0]*(m+2)]
visited=[[m*n]*(m+2)]+[[False]+[0 for i in range(m)]+[False]for i in range(n)]+[[m*n]*(m+2)]
visited[0][0]=1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
mn=[]

def bfs(x,y,cnt):
    if x==m and y==n:
        mn.append(cnt+1)
        return
    visited[y][x]=cnt
    queue=[[x,y]]
    queue=deque(queue)
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            x2,y2=x+dx[i],y+dy[i]
            if visited[y2][x2]==0 and maze[y2][x2]=='1':
                visited[y2][x2]=visited[y][x]+1
                queue.append([x2,y2])
        for xy in queue:
            bfs(xy[0],xy[1],cnt+1)

bfs(1,1,1)

print(min(mn))
'''

import sys
from collections import *

input=sys.stdin.readline

n,m=map(int,input().split())
maze=[input().rstrip() for i in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=[[0,0]]
visited[0][0]=1

while queue:
    queue=deque(queue)
    x,y=queue.popleft()
    visited[x][y]
    if x==n-1 and y == m-1:
        print(visited[x][y])
    for i in range(4):
        x2=x+dx[i]
        y2=y+dy[i]
        if 0<=x2<n and 0<=y2<m:
            if visited[x2][y2]==0 and maze[x2][y2]=='1':
                visited[x2][y2]=visited[x][y]+1
                queue.append([x2,y2])
    

'''
# 가져온 코드
from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
'''

from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

def bfs(dots,k):
    queue=deque([])
    for x,y in dots:
        vi[k][y][x]=0
        queue.append([x,y])
    dist=1
    while queue:
        le=len(queue)
        for _ in range(le):
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if -1<nx<m and -1<ny<n:
                    if vi[k][ny][nx]==-1:
                        vi[k][ny][nx]=dist
                        queue.append([nx,ny])
        dist+=1

dx,dy=[0,0,-1,1],[1,-1,0,0]

n,m=map(int,input().split())
arr=[list(map(int,list(input().rstrip()))) for i in range(n)]

vi=[[[-1]*m for i in range(n)] for j in range(10)]

dots=[[] for i in range(10)]

for i in range(n):
    for j in range(m):
        dots[arr[i][j]].append([j,i])

for i in range(10):
    bfs(dots[i],i)

q=int(input())
for i in range(q):
    line=input().rstrip().split()
    y=int(line[0])-1
    x=int(line[1])-1
    order=int(line[2])
    for i in range(order):
        print(vi[int(line[-1][i])][y][x],end=' ')
    print()

from sys import stdin
from collections import deque
input=stdin.readline

def bfs(X,Y):
    loc=m*Y+X
    queue=deque([[X,Y,0]])
    vi[Y][X]=now
    dist[loc][arr[Y][X]]=0
    findout=0
    while queue:
        x,y,d=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]<now:
                    vi[ny][nx]=now
                    if dist[loc][arr[ny][nx]]==-1:
                        dist[loc][arr[ny][nx]]=d+1
                        findout+=1
                        if findout==len(kind):
                            return
                    queue.append([nx,ny,d+1])

dx,dy=[0,0,-1,1],[1,-1,0,0]

n,m=map(int,input().split())
arr=[list(map(int,list(input().rstrip()))) for i in range(n)]
kind=set()

for i in arr:
    for j in i:
        kind.add(j)

vi=[[0]*m for i in range(n)]
now=1
dist=[[-1]*(10) for i in range(n*m)]

for i in range(n):
    for j in range(m):
        bfs(j,i)
        now+=1

q=int(input())
for i in range(q):
    line=input().rstrip().split()
    y=int(line[0])-1
    x=int(line[1])-1
    loc=y*m+x
    order=int(line[2])
    res=0
    for i in range(order):
        print(dist[loc][int(line[-1][i])],end=' ')
    print()

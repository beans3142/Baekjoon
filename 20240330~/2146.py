from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(X,Y):
    queue=deque([(X,Y)])
    group=[(X,Y)]
    vi[Y][X]=1 
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                if vi[ny][nx]==0 and arr[ny][nx]==1:
                    vi[ny][nx]=1
                    queue.append((nx,ny))
                    group.append((nx,ny))
    return group


def getdist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]

vi=[[0]*(n) for i in range(n)]
groups=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and vi[i][j]==0:
            groups.append(bfs(j,i))

ans=1e10
le=len(groups)

for i in range(le):
    for j in range(i+1,le):
        for dot1 in groups[i]:
            for dot2 in groups[j]:
                dist=getdist(dot1[0],dot1[1],dot2[0],dot2[1])-1
                ans=min(ans,dist)
print(ans)
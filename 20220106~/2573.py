from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
vi=[[0 for i in range(m)] for i in range(n)]
time=0

def bfs(X,Y):
    vi[Y][X]=time+1
    queue=deque([(X,Y)])
    melt=[]
    while queue:
        x,y=queue.popleft()
        near=0
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if -1<nx<m and -1<ny<n:
                if arr[ny][nx]!=0 and vi[ny][nx]<=time:
                    vi[ny][nx]=time+1
                    queue.append((nx,ny))
                elif arr[ny][nx]==0:
                    near+=1
        melt.append((x,y,near))

    for x,y,minus in melt:
        arr[y][x]=max(0,arr[y][x]-minus)

while True:
    group=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and vi[i][j]<=time:
                group+=1
                bfs(j,i)

    if group>1:
        break
    elif not group:
        break
    time+=1

if group>1:
    print(time)
else:
    print(0)

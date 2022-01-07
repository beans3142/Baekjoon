from sys import stdin
from collections import deque
input=stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,l,r=map(int,input().split())
arr=[]
cnt=0

for i in range(n):
    arr.append(list(map(int,input().split())))

while True:
    v=[[0 for i in range(n)] for i in range(n)]
    moved=False
    case=[]
    for i in range(n):
        for j in range(n):
            if v[i][j]==0:
                v[i][j]=1
                union=[]
                queue=deque([[j,i]])
                while queue:
                    x,y=queue.popleft()
                    union.append((x,y))
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if -1<nx<n and -1<ny<n:
                            if v[ny][nx]==0 and l<=abs(arr[ny][nx]-arr[y][x])<=r:
                                v[ny][nx]=1
                                union.append((nx,ny))
                                queue.append([nx,ny])
                if len(union)>1:
                    s=0
                    for loc in set(union):
                        s+=arr[loc[1]][loc[0]]
                    case.append([s,set(union)])
    for _ in case:
        total=_[0]
        loc=_[1]
        for locate in loc:
            x=locate[0]
            y=locate[1]
            arr[y][x]=total//len(loc)
    if not case:
        break
    cnt+=1

print(cnt)

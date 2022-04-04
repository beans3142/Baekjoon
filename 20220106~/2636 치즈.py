from sys import stdin
from collections import deque
from copy import deepcopy
input=stdin.readline

n,m=map(int,input().split())
arr=[[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for i in range(n)]+[[0]*(m+2)]
tmp=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans=[]
while True:
    cnt=0
    melt=False
    queue=deque([[0,0]])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<=m+1 and -1<ny<=n+1:
                if arr[ny][nx]!=1 and arr[ny][nx]!=2+tmp:
                    arr[ny][nx]=2+tmp
                    queue.append([nx,ny])
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[i][j]==1:
                for k in range(4):
                    if arr[i+dy[k]][j+dx[k]]==2+tmp:
                        arr[i][j]=0
                        cnt+=1
                        melt=True
                        break

    if melt:
        ans.append(cnt)
        tmp+=1
        continue
    break

print(tmp)

print(ans[-1])

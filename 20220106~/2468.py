from sys import *
from collections import *
dx=[0,0,1,-1]
dy=[1,-1,0,0]
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
vi=[[0 for i in range(n)] for j in range(n)]
ans=0

for h in range(101):
    cnt=0
    for i in range(n):
        for j in range(n):
            if vi[i][j]<=h and arr[i][j]>h:
                vi[i][j]=h+1
                queue=deque([(j,i)])
                while queue:
                    x,y=queue.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if -1<nx<n and -1<ny<n:
                            if vi[ny][nx]<=h and arr[ny][nx]>h:
                                vi[ny][nx]=h+1
                                queue.append((nx,ny))
                cnt+=1
    ans=max(ans,cnt)

print(ans)

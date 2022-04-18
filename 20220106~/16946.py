from sys import stdin
from collections import *
input=stdin.readline

def bfs(X,Y):
    vi[Y][X]=1
    group[(X,Y)]=groupno
    groupsize[groupno]+=1
    queue=deque([[X,Y]])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]==0 and arr[ny][nx]=='0':
                    group[(nx,ny)]=groupno
                    groupsize[groupno]+=1
                    vi[ny][nx]=1
                    queue.append((nx,ny))
    
    

n,m=map(int,input().split())

arr=[input().rstrip() for i in range(n)]
vi=[[0 for i in range(m)] for i in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

group=defaultdict(int)
groupno=1
groupsize=defaultdict(int)

for i in range(n):
    for j in range(m):
        if vi[i][j]==0 and arr[i][j]=='0':
            bfs(j,i)
            groupno+=1


for i in range(n):
    for j in range(m):
        if arr[i][j]=='0':
            print('0',end='')
        else:
            cnt=1
            same=defaultdict(int)
            for x,y in [(j,i+1),(j,i-1),(j+1,i),(j-1,i)]:
                if -1<x<m and -1<y<n:
                    if same[group[(x,y)]]==0:
                        cnt+=groupsize[group[(x,y)]]
                        same[group[(x,y)]]=1
            
            print(cnt%10,end='')
    print()
                    

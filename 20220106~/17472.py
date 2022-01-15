from sys import stdin
from collections import deque,defaultdict
from math import inf
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(X,Y):
    global th
    queue=deque([[X,Y]])
    v[Y][X]=1
    arr[Y][X]=th
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if v[ny][nx]==0 and arr[ny][nx]==1:
                    arr[ny][nx]=th
                    v[ny][nx]=1
                    queue.append([nx,ny])
    th+=1

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b,val):
    global canremove
    c=a
    d=b
    a=find(a)
    b=find(b)

    if a<b:
        par[b]=a
        mst[c][d]=mst[d][c]=val
    elif a>b:
        par[a]=b
        mst[c][d]=mst[d][c]=val

n,m=map(int,input().split())
th=1
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

v=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if v[i][j]==0 and arr[i][j]==1:
            bfs(j,i)

rel={i:defaultdict(int) for i in range(1,th)}

for j in range(m):
    queue=[]
    for k in range(n):
        if arr[k][j]!=0:
            if queue:
                if queue[0]!=arr[k][j]:
                    if len(queue)-1>1:
                        if rel[queue[0]][arr[k][j]]==0:
                            rel[queue[0]][arr[k][j]]=rel[arr[k][j]][queue[0]]=len(queue)-1
                        else:
                            rel[queue[0]][arr[k][j]]=rel[arr[k][j]][queue[0]]=min(len(queue)-1,rel[queue[0]][arr[k][j]])
                    queue=[arr[k][j]]
                else:
                    queue=[arr[k][j]]
            else:
                queue=[arr[k][j]]
        elif queue:
            queue.append(0)

for i in range(n):
    queue=[]
    for k in range(m):
        if arr[i][k]!=0:
            if queue:
                if queue[0]!=arr[i][k]:
                    if len(queue)-1>1:
                        if rel[queue[0]][arr[i][k]]==0:
                            rel[queue[0]][arr[i][k]]=rel[arr[i][k]][queue[0]]=len(queue)-1
                        else:
                            rel[queue[0]][arr[i][k]]=rel[arr[i][k]][queue[0]]=min(len(queue)-1,rel[queue[0]][arr[i][k]])
                    queue=[arr[i][k]]
                else:
                    queue=[arr[i][k]]
            else:
                queue=[arr[i][k]]
        elif queue:
            queue.append(0)

node=[]

for i in rel:
    for j in rel[i]:
        node.append([rel[i][j],i,j])

node.sort()

par=list(range(th))

mst={i:defaultdict(int) for i in range(1,th)}

for val,a,b in node:
    union(a,b,val)

total=0
for i in mst:
    for j in mst[i]:
        total+=mst[i][j]

for i in range(1,th):
    find(i)

if len(set(par))>2:
    print(-1)
else:
    print(total//2)

from sys import stdin
from heapq import *
from collections import *
input=stdin.readline

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b,val):
    a=find(a)
    b=find(b)
    if par[a]<par[b]:
        par[b]=a
        graph[b][a]=val
        graph[a][b]=val
    elif par[b]<par[a]:
        par[a]=b
        graph[a][b]=val
        graph[b][a]=val
    else:
        return -1

n=int(input())
graph=[defaultdict(int) for i in range(n+1)]

par=[i for i in range(n+1)]
xarr=[]
yarr=[]
zarr=[]

for i in range(1,n+1):
    x,y,z=map(int,input().split())
    xarr.append([x,i])
    yarr.append([y,i])
    zarr.append([z,i])

xarr.sort()
yarr.sort()
zarr.sort()

hq=[]

for i in range(1,n):
    xdif=abs(xarr[i-1][0]-xarr[i][0])
    heappush(hq,(xdif,xarr[i-1][-1],xarr[i][-1]))
    ydif=abs(yarr[i-1][0]-yarr[i][0])
    heappush(hq,(ydif,yarr[i-1][-1],yarr[i][-1]))
    zdif=abs(zarr[i-1][0]-zarr[i][0])
    heappush(hq,(zdif,zarr[i-1][-1],zarr[i][-1]))

while hq:
    dif,a,b=heappop(hq)
    union(a,b,dif)

for i in range(n):
    find(i+1)
ans=0
queue=deque([1])
vi=[0]*(n+1)
vi[1]=1

while queue:
    nxt=queue.popleft()
    for i in graph[nxt]:
        if vi[i]==0:
            vi[i]=1
            ans+=graph[nxt][i]
            queue.append(i)

print(ans)

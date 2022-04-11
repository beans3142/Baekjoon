from sys import *
from collections import *
from heapq import *
setrecursionlimit(100000)
input=stdin.readline

def dfs(x,wei):
    vi[x]=1
    mxweight[x]=wei
    for i in graph[x]:
        if vi[i]==0:
            dfs(i,min(wei,graph[x][i]))

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(val,a,b):
    a=find(a)
    b=find(b)
    if par[a]<par[b]:
        par[b]=a
        graph[b][a]=-val
        graph[a][b]=-val
    elif par[b]<par[a]:
        par[a]=b
        graph[b][a]=-val
        graph[a][b]=-val
    

n,m=map(int,input().split())
par=[i for i in range(n+1)]
graph=[defaultdict(int) for i in range(n+1)]
hq=[]
mxweight=[0]*(n+1)
vi=[0]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    heappush(hq,[-c,a,b])

while hq:
    union(*heappop(hq))

for i in graph[1]:
    dfs(1,graph[1][i])

print(mxweight[n])

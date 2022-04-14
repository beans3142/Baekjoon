from sys import stdin
from collections import *
from heapq import *
input=stdin.readline

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b,c):
    graph[a][b]=graph[b][a]=c
    a=find(a)
    b=find(b)
    
    if par[a]>par[b]:
        par[a]=b
    elif par[a]<par[b]:
        par[b]=a

def bfs(x):
    vi=[0]*(n+1)
    vi[x]=1
    queue=deque([(x,1e10)])
    while queue:
        now,total=queue.popleft()
        if now==e:
            return total
        for i in graph[now]:
            if vi[i]==0:
                vi[i]=1
                queue.append([i,min(total,graph[now][i])])
        
        

n,m=map(int,input().split())
s,e=map(int,input().split())
par=[i for i in range(n+1)]
graph=[defaultdict(int) for i in range(n+1)]
hq=[]

for i in range(m):
    a,b,c=map(int,input().split())
    heappush(hq,[-c,a,b])

while hq:
    c,a,b=heappop(hq)
    if find(a)!=find(b):
        union(a,b,-c)

print(bfs(s))


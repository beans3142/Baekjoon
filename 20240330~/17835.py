from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict
input=stdin.readline

inf=float('inf')

n,m,k=map(int,input().split())
graph=[defaultdict(int) for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    if graph[b][a]: graph[b][a]=min(graph[b][a],c)
    else: graph[b][a]=c
vi=[inf for i in range(n+1)]

hq=[]

for i in list(map(int,input().split())):
    heappush(hq,(0,i))
    vi[i]=0

while hq:
    cost,now=heappop(hq)
    if vi[now]<cost:
        continue
    for nxt in graph[now]:
        nxtcost=cost+graph[now][nxt]
        if nxtcost<vi[nxt]:
            vi[nxt]=nxtcost
            heappush(hq,(nxtcost,nxt))

vi[0]=0
print(vi.index(max(vi)))
print(max(vi))

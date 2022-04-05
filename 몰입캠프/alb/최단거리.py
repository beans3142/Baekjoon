from sys import stdin
from heapq import heappop,heappush
input=stdin.readline
inf=float('inf')

n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
s,e=map(int,input().split())
queue=[(0,s)]
dist=[inf]*n
dist[s]=0

while queue:
    totaldist,now=heappop(queue)
    if dist[now]<totaldist:
        continue
    for i in graph[now]:
        if dist[i]==inf:
            dist[i]=totaldist+1
            heappush(queue,(totaldist+1,i))

print(dist[e])

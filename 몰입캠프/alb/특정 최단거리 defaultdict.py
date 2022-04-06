from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict
input=stdin.readline

inf=float('inf')
n,m=map(int,input().split())
graph={i:defaultdict(int) for i in range(1,n+1)}

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=graph[b][a]=c if graph[a][b] == 0 else min(graph[a][b],c)

def dijkstra(s):
    dist=[inf]*(n+1)
    dist[s]=0
    queue=[(0,s)]
    while queue:
        totaldist,now=heappop(queue)
        if dist[now]<totaldist:
            continue
        for i in graph[now]:
            nextdist=totaldist+graph[now][i]
            if dist[i]>nextdist:
                dist[i]=nextdist
                heappush(queue,(nextdist,i))
    return dist

a,b=map(int,input().split())
start=dijkstra(1)
A=dijkstra(a)
B=dijkstra(b)
ans=min(start[a]+A[b]+B[n],start[b]+B[a]+A[n])
print(ans if ans!= inf else -1)
                

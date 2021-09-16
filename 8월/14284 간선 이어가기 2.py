from sys import stdin
from heapq import heappop,heappush
from math import inf
input=stdin.readline

V,E=map(int,input().split())
#graph={i:[]for i in range(1,V+1)}
graph=[[]for _ in range(V+1)]

for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])
    
start,end=map(int,input().split())

def diikstra(start):
    queue=[(start,0)]
    zzarb=[inf]*(V+1)
    zzarb[start]=0
    while queue:
        now,length=heappop(queue)
        if length>zzarb[now]:
            continue
        for node,next_len in graph[now]:
            total=length+next_len
            if total<zzarb[node]:
                zzarb[node]=total
                heappush(queue,[node,length+next_len])
    return zzarb

a=diikstra(start)

print(a[end])

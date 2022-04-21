from sys import stdin
from collections import deque
from heapq import heappop,heappush
input=stdin.readline

inf=float('inf')

def dijk():
    vi=[inf]*(n)
    vi[s]=0
    queue=[(0,s)]
    while queue:
        nowdist,now=heappop(queue)
        if vi[now]<nowdist:
            continue
        for i in graph[now]:
            nxtdist=nowdist+graph[now][i]
            if nxtdist<vi[i]:
                vi[i]=nxtdist
                heappush(queue,(nxtdist,i))
    return vi

def bfs():
    queue=deque([(d,0)])
    vi=[0]*n
    vi[d]=1
    while queue:
        now,nowdist=queue.popleft()
        for i in rgraph[now]:
            try:
                if graph[i][now]:
                    if dist[i]+rgraph[now][i]+nowdist==dist[d]:                   
                        del graph[i][now]
                        queue.append([i,nowdist+rgraph[now][i]])
            except:
                pass


while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    s,d=map(int,input().split())
    graph=[{} for i in range(n)]
    rgraph=[{} for i in range(n)]

    for i in range(m):
        u,v,p=map(int,input().split())
        graph[u][v]=p
        rgraph[v][u]=p

    dist=dijk()
    bfs()
    
    
    mn=dijk()
    print(mn[d] if mn[d] != inf else -1)

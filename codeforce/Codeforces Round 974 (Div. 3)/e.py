from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import combinations,permutations

inf=float('inf')

for _ in range(int(input())):
    n,m,h=map(int,input().split())
    horse=set(map(int,input().split()))
    graph=[[] for i in range(n+1)]
    
    for i in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    hq=[(0,0,1,0)]
    vi=[[[inf]*(n+1) for i in range(2)] for i in range(2)]
    vi[0][0][1]=vi[0][1][n]=0
    ans=inf
    while hq:
        ride,cost,now,typ=heappop(hq)
        if now in horse:
            ride=1
        if vi[ride][typ][now]<cost:
            continue
        for nxt,nxtc in graph[now]:
            nxtcost=cost+(nxtc//2 if ride else nxtc)
            if vi[ride][typ][nxt]>nxtcost:
                vi[ride][typ][nxt]=nxtcost
                heappush(hq,(ride,nxtcost,nxt,typ))
    hq=[(0,0,n,1)]
    while hq:
        ride,cost,now,typ=heappop(hq)
        if now in horse:
            ride=1
        if vi[ride][typ][now]<cost:
            continue
        for nxt,nxtc in graph[now]:
            nxtcost=cost+(nxtc//2 if ride else nxtc)
            if vi[ride][typ][nxt]>nxtcost:
                vi[ride][typ][nxt]=nxtcost
                heappush(hq,(ride,nxtcost,nxt,typ))
    
    for i in range(1,n+1):
        for j in range(2):
            for k in range(2):
                ans=min(ans,max(vi[j][0][i],vi[k][1][i]))
        
    print(ans if ans!=inf else -1)

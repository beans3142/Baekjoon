from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    con=[0]*(n+1)
    graph=[[] for i in range(n+1)]
    safeArea=[1]*(n+1)
    for _ in range(n):
        u,v=map(int,input().split())
        con[u]+=1
        con[v]+=1
        graph[u].append(v)
        graph[v].append(u)
    
    toplo=deque([])
    for i in range(1,n+1):
        if con[i]==1:
            toplo.append(i)

    while toplo:
        now=toplo.popleft()
        safeArea[now]=0
        for nxt in graph[now]:
            con[nxt]-=1
            if con[nxt]==1:
                toplo.append(nxt)
    
    queue1=deque([a])
    queue2=deque([b])
    vi=[0]*(n+1)
    vi[b]=2
    vi[a]=1
    ans=False
    while queue1 or queue2:
        le1=len(queue1)
        for i in range(le1):
            now=queue1.popleft()
            for nxt in graph[now]:
                if vi[nxt]==0:
                    vi[nxt]=1
                    queue1.append(nxt)
        
        le2=len(queue2)
        for i in range(le2):
            now=queue2.popleft()
            if safeArea[now] and vi[now]!=1:
                ans=True
            for nxt in graph[now]:
                if vi[nxt]==0:
                    vi[nxt]=2
                    queue2.append(nxt)
    if ans:
        print("YES")
    else:
        print("NO")

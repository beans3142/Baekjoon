from sys import stdin
from heapq import heappop,heappush
from math import inf
input=stdin.readline

n,m,x=map(int,input().split())

rel=[[] for i in range(n)]
for i in range(m):
    a,b,t=map(int,input().split())
    rel[a-1].append((b-1,t))

def di(start):
    queue=[(0,start)]
    fromx=[inf for i in range(n)]
    fromx[start]=0
    while queue:
        time,now=heappop(queue)
        if fromx[now]<time:
            continue
        for to,spend in rel[now]:
            ntime=time+spend
            if fromx[to]>ntime:
                fromx[to]=ntime
                heappush(queue,(ntime,to))
    return fromx

ans=0
from_x=di(x-1)
for i in range(n):
    to_x=di(i)
    ans=max(to_x[x-1]+from_x[i],ans)
print(ans)

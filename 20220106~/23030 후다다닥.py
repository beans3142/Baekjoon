from sys import stdin
from collections import defaultdict
from heapq import heappop,heappush
from math import inf
input=stdin.readline

n=int(input())
stop_cnt=list(map(int,input().split()))
val={}
rel=defaultdict(list)
for i in range(n):
    for j in range(stop_cnt[i]):
        no=i+1
        nono=j+1
        val[(no,nono)]=inf
        rel[(no,nono)]
        if nono>1:
            rel[(no,nono)].append((no,nono-1))
        if nono<stop_cnt[i]:
            rel[(no,nono)].append((no,nono+1))

m=int(input())
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    rel[(x1,y1)].append((x2,y2))
    rel[(x2,y2)].append((x1,y1))

k=int(input())
for i in range(k):
    t,u1,u2,v1,v2=map(int,input().split())
    queue=[(0,u1,u2)]
    while queue:
        time,no,nono=heappop(queue)
        if val[(no,nono)]<time:
            continue
        val[(no,nono)]=time
        for i in rel[(no,nono)]:
            if i[0]==no:
                add=1
            else:
                add=t
            if time+add<val[i]:
                val[i]=time+add
                heappush(queue,(time+add,i[0],i[1]))
    print(val[(v1,v2)])
    break
    for j in val:
        val[j]=inf

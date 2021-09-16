import sys
from heapq import heappush,heappop

input=sys.stdin.readline
inf=sys.maxsize

n,m=map(int,input().split())

city={i:[]for i in range(1,n+1)}

for i in range(m):
    u,v,w=map(int,input().split())
    city[u].append([v,w])
    city[v].append([u,w])

n1,n2=map(int,input().split())

def diik(start):
    cost=[inf] *(n+1)
    cost[start]=0

    travel=[(0,start)]

    while travel:
        price,now=heappop(travel)
        if cost[now]<price:
            continue
        for nextcity,val in city[now]:
            if cost[nextcity]>price+val:
                cost[nextcity]=price+val
                heappush(travel,(price+val,nextcity))
    return cost

first=diik(1)
going1,going2=diik(n1),diik(n2)
road=min(going1[n2]+going2[n]+first[n1],going2[n1]+going1[n]+first[n2])
print(road if road<inf else -1)

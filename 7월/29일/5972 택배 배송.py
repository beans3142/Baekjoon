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

cost=[inf]*(n+1)
cost[1]=0

travel=[(0,1)]

while travel:
    price,now,vi_list=heappop(travel)
    if cost[now]<price:
        continue
    for nextcity,val in city[now]:
        if cost[nextcity]>price+val:
            cost[nextcity]=price+val
            heappush(travel,(price+val,nextcity,vi_list+[nextcity]))

    
print(cost[n])

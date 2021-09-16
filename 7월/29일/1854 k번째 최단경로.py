import sys
from heapq import heappush,heappop

input=sys.stdin.readline
inf=sys.maxsize

n,m,k=map(int,input().split())

city={i:[]for i in range(1,n+1)}

for i in range(m):
    u,v,w=map(int,input().split())
    city[u].append([v,w])
    #city[v].append([u,w])

cost=[[]for i in range(n+1)]
cost[1].append(0)

travel=[(0,1)]

while travel:
    price,now=heappop(travel)
    if len(cost[now])>k:
        continue
    for nextcity,val in city[now]:
        if len(cost[nextcity])<k:
            cost[nextcity].append(price+val)
            heappush(travel,(price+val,nextcity))

    
for i in range(1,n+1):
    if len(cost[i])<k:
        print(-1)
    else:
        print(sorted(cost[i])[k-1])
        

import sys
from heapq import heappush,heappop

input=sys.stdin.readline
inf=sys.maxsize

n,m=map(int,input().split())

city={i:[]for i in range(1,n+1)}

for i in range(m):
    u,v,w,d=map(int,input().split())
    city[u].append([v,w,d])
    city[v].append([u,w,d])

cost=[inf]*(n+1)
cost[1]=0

travel=[(0,1,False)]

while travel:
    price,now,don_ggas_eat=heappop(travel)
    '''
    if cost[now]<price:
        continue
        '''
    for nextcity,val,ggas in city[now]:
        if cost[nextcity]>price+val:
            cost[nextcity]=price+val
            heappush(travel,(price+val,nextcity,don_ggas_eat))
    if don_ggas_eat==False:
        for nextcity,val,ggas in city[now]:
            if cost[nextcity]>price+val-ggas:
                cost[nextcity]=price+val-ggas
                heappush(travel,(price+val-ggas,nextcity,True))
        
for i in range(2,len(cost)):
    print(cost[i])

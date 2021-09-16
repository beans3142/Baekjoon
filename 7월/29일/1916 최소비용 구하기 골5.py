import sys
from heapq import heappush,heappop

input=sys.stdin.readline
inf=sys.maxsize

n=int(input())
m=int(input())

city={i:[]for i in range(1,n+1)}

for i in range(m):
    u,v,w=map(int,input().split())
    city[u].append([v,w])
    #city[v].append([u,w])

start,end=map(int,input().split())

cost=[[inf,[]]for i in range(n+1)]
cost[start]=[0,[start]]

travel=[(0,start,[start])]

while travel:
    price,now,vi_list=heappop(travel)
    if cost[now][0]<price:
        continue
    for nextcity,val in city[now]:
        if cost[nextcity][0]>price+val:
            cost[nextcity][0]=price+val
            cost[nextcity][1]=vi_list+[nextcity]
            heappush(travel,(price+val,nextcity,vi_list+[nextcity]))

    
print(cost[end][0])
print(len(cost[end][1]))
print(*cost[end][1])

from sys import stdin
from heapq import heappush,heappop
from math import inf
input=stdin.readline

n,m=map(int,input().split())
time_table={i:[]for i in range(n)}
route_table=[[0 for i in range(n)]for j in range(n)]

for i in range(m):
    x,y,time_spend=map(int,input().split())
    time_table[x-1].append([y-1,time_spend])
    time_table[y-1].append([x-1,time_spend])

for i in range(n):
    queue=[[0,i]]
    v_place=[inf for i in range(n)]
    v_place[i]=0
    while queue:
        s,now=heappop(queue)
        print(v_place)
        for can_go,time_spend in time_table[now]:
            if s+time_spend<v_place[can_go]:
                v_place[can_go]=s+time_spend
                route_table[can_go][i]=now
                heappush(queue,[s+time_spend,can_go])

for i in range(n):
    for j in range(n):
        print('-' if i==j else route_table[i][j]+1,end=' ' if j!=n-1 else'\n')
    

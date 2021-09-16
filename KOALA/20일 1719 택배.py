from sys import stdin
from collections import deque
from heapq import heappush,heappop
from math import inf

input=stdin.readline

n,m=map(int,input().split())
time_table=[[0 for i in range(n)]for j in range(n)]
route_table=[[[inf,inf] for i in range(n)]for j in range(n)]

for i in range(m):
    x,y,time_spend=map(int,input().split())
    time_table[y-1][x-1]=time_table[x-1][y-1]=time_spend

for i in range(n):
    queue=[[0,i,[]]]
    while queue:
        time_spend,nowlocate,start_at=heappop(queue)
        
        if route_table[i][nowlocate][0]<time_spend:
            continue
        if start_at:
            if True:
                print(i,nowlocate,start_at)
            #if time_spend<route_table[i][nowlocate][1]:
                route_table[i][nowlocate][0]=start_at[0]
                route_table[i][nowlocate][1]=time_spend
        for j in range(n):
            if route_table[i][j][0]!=inf:
                continue
            if time_table[nowlocate][j]!=0 and i!=j:
                heappush(queue,[time_spend+time_table[nowlocate][j],j,start_at+[j]])

for i in range(n):
    for j in range(n):
        print('-' if i==j else route_table[i][j][0]+1,end=' ')
    print()

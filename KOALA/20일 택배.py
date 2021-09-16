from sys import stdin
from collections import deque
from heapq import heappush,heappop
input=stdin.readline

n,m=map(int,input().split())
time_table=[[0 for i in range(n)]for j in range(n)]
route_table=[[-1 for i in range(n)]for j in range(n)]

for i in range(m):
    x,y,time_spend=map(int,input().split())
    time_table[y-1][x-1]=time_table[x-1][y-1]=time_spend

for i in range(n):
    queue=[[0,i]]
    while queue:
        time_spend,nowlocate=heappop(queue)
        for j in range(n):
            if time_table[nowlocate][j]==1:
                heappush(queue,[])

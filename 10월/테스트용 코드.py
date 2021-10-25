from sys import stdin
from heapq import *

input=stdin.readline
dx,dy=[0,0,1,-1],[1,-1,0,0]

n=int(input())
load=[list(map(int,input().split())) for i in range(n)]
value_table=[[-1 for i in range(n)]for j in range(n)]

v=[[0,0,0]]

while True:
    lean,x,y=heappop(v)
    if value_table[y][x]!=-1:
        continue
    if y==n-1 and x==n-1:
        print(lean)
        break
    value_table[y][x]=lean
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if value_table[ny][nx]!=-1:
                continue
            heappush(v,[max(abs(load[y][x]-load[ny][nx]),lean),nx,ny])

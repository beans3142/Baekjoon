from sys import stdin
from heapq import *
from collections import deque
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
vi=[[0 for i in range(n)] for j in range(n)]
queue=[(0,0,0)]
ans=0
vi[0][0]=1

def gd(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

while queue:
    dis,x,y=heappop(queue)
    dist=arr[y][x]
    if x==n-1 and y==n-1:
        ans+=1
        continue
    if x+dist<n:
        if vi[y][x+dist]==0:
            heappush(queue,[gd(0,0,x+dist,y),x+dist,y])
        vi[y][x+dist]+=vi[y][x]
    if y+dist<n:
        if vi[y+dist][x]==0:
            heappush(queue,[gd(0,0,x,y+dist),x,y+dist])
        vi[y+dist][x]+=vi[y][x]

print(vi[-1][-1])

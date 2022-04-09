from sys import *
from collections import *
#from math import *
#from itertools import *
#from heapq import *
#from bisect import *
#setrecursionlimit(100000)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
vi=[[0 for i in range(n)] for j in range(n)]
ans=0

def bfs(X,Y):
    vi[Y][X]=h+1
    queue=deque([(X,Y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                if vi[ny][nx]<=h and arr[ny][nx]>h:
                    vi[ny][nx]=h+1
                    queue.append((nx,ny))


for h in range(1,101):
    cnt=0
    for i in range(n):
        for j in range(n):
            if vi[i][j]<=h and arr[i][j]>h:
                bfs(j,i)
                cnt+=1
    ans=max(ans,cnt)

print(ans)

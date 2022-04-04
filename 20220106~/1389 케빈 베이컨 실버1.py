import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

friend=[[0 for i in range(n)] for i in range(n)]

mintemp=1000000

for i in range(m):
    x,y=map(int,input().split())
    friend[x-1][y-1]=friend[y-1][x-1]=1


def bfs(N,t):
    visited[N]=True
    queue=deque([[N,t]])
    kavin_bacon=0
    while queue:
        nowperson,tmp=queue.popleft()
        for i in range(n):
            if friend[nowperson][i]==1 and visited[i]==0:
                visited[i]=True
                queue.append([i,tmp+1])
                kavin_bacon+=tmp+1
    return kavin_bacon
    

for i in range(n):
    visited=[0 for j in range(n)]
    bacon=bfs(i,0)
    if bacon<mintemp:
        kavin=i+1
        mintemp=bacon

print(kavin)

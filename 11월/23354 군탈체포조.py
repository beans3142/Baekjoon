from sys import stdin
from heapq import heappop,heappush
from itertools import permutations
from math import inf
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())

arr=[list(map(int,input().split())) for i in range(n)]

tar=[]
boodae=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            tar.append([j,i])
        elif arr[i][j]==-1:
            boodae=[j,i]

arr[boodae[1]][boodae[0]]=0

def dijk(X,Y):
    v=[[inf]*n for i in range(n)]
    queue=[[0,X,Y]]
    while queue:
        dist,x,y=heappop(queue)
        if v[y][x]<dist:
            continue
        if v[boodae[1]][boodae[0]]!=inf:
            end=True
            for j in tar:
                if v[j[1]][j[0]]==inf:
                    end=False
                    break
            if end:
                return v
        v[y][x]=dist
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                adist=dist+arr[ny][nx]
                if v[ny][nx]>adist:
                    v[ny][nx]=adist
                    heappush(queue,(adist,nx,ny))

    return v

each_dist=[dijk(boodae[0],boodae[1])]
for i in tar:
    each_dist.append(dijk(i[0],i[1]))

case=list(permutations([i for i in range(len(tar))],len(tar)))

ans=inf
for i in case:
    dist=0
    befx=boodae[0]
    befy=boodae[1]
    bef=0
    for j in range(len(i)):
        nowplace=tar[i[j]]
        nowx,nowy=nowplace[0],nowplace[1]
        dist+=each_dist[bef][nowy][nowx]
        befx=nowx
        befy=nowy
        bef=i[j]+1
    dist+=each_dist[bef][boodae[1]][boodae[0]]
    ans=min(ans,dist)

print(ans)

import sys
from collections import deque

load=[list(map(int,input().split()))for i in range(int(input()))]
dx,dy=[-1,1,0,0],[0,0,-1,1]
v=[[0 for i in range(len(load))]for j in range(len(load))]
v[0][0]=1
queue=deque([[0,0,load[0][0],0,v]])
mnprice=1000000000*1000

while queue:
    x,y,height,price,V=queue.popleft()
    print(V)
    if x==len(load)-1 and y==len(load)-1:
        mnprice=min(price,mnprice)
        continue
    for i in range(4):
        if 0<=x+dx[i]<len(load) and 0<=y+dy[i]<len(load):
            if V[y+dy[i]][x+dx[i]]==0:
                gyungsa=0 if load[y+dy[i]][x+dx[i]]<height else load[y+dy[i]][x+dx[i]]-height
                V[y+dy[i]][x+dx[i]]=1
                queue.append([x+dx[i],y+dy[i],load[y+dy[i]][x+dx[i]],price+gyungsa,V])

from sys import stdin
from collections import deque
input=stdin.readline

d=[0,0,2,1,3]
cost=[0,1,2,1]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

m,n=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(m)]
order=[[[-1 for i in range(n)]for i in range(m)]for i in range(4)]

sy,sx,sd=map(int,input().split())
sy-=1
sx-=1
sd=d[sd]
ey,ex,ed=map(int,input().split())
ed=d[ed]
ey-=1
ex-=1

queue=deque([])

for i in range(4):
    nd=(sd+i)%4
    order[nd][sy][sx]=cost[i]
    queue.append([sx,sy,nd,cost[i]])

while queue:
    x,y,dr,t=queue.popleft()
    for i in range(4):
        ndr=(dr+i)%4
        nx=x
        ny=y
        if order[ndr][ny][nx]==-1:
            order[ndr][ny][nx]=t+cost[i]
            queue.append([nx,ny,ndr,t+cost[i]])
        else:
            if t+cost[i]<order[ndr][ny][nx]:
                order[ndr][ny][nx]=t+cost[i]
                queue.append([nx,ny,ndr,order[ndr][ny][nx]])
        for j in range(1,4):
            nx+=dx[ndr]
            ny+=dy[ndr]
            if -1<nx<n and -1<ny<m:
                if arr[ny][nx]==0:
                    if order[ndr][ny][nx]==-1:
                        order[ndr][ny][nx]=t+cost[i]+1
                        queue.append([nx,ny,ndr,order[ndr][ny][nx]])
                    else:
                        if t+cost[i]+1<order[ndr][ny][nx]:
                            order[ndr][ny][nx]=t+cost[i]+1
                            queue.append([nx,ny,ndr,order[ndr][ny][nx]])                  
                else:
                    break
'''
for i in order:
    for j in i:
        print(j)
    print()'''

print(order[ed][ey][ex])

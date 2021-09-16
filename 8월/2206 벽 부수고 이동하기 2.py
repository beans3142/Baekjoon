from sys import stdin,maxsize
from heapq import heappop,heappush
input=stdin.readline
inf=maxsize
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,input().split())

arr=[list(map(int,list(input().rstrip()))) for i in range(n)]
val=[[inf]*m for i in range(n)]
queue=[[0,1,0,0]]

while queue:
    broke,dist,x,y=heappop(queue)
    if val[y][x]<dist:
        continue
    val[y][x]=dist
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        n_dist=dist+1
        if -1<nx<m and -1<ny<n:
            if arr[ny][nx]==1:
                if not broke:
                    if val[ny][nx]>n_dist:
                        val[ny][nx]=n_dist
                        heappush(queue,[1,n_dist,nx,ny])
            elif arr[ny][nx]==0:
                if val[ny][nx]>n_dist:
                    val[ny][nx]=n_dist
                    heappush(queue,[broke,n_dist,nx,ny])
    
print(val[-1][-1] if val[-1][-1] != inf else -1)

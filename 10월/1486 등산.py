from sys import stdin
from heapq import heappush,heappop
from math import inf
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

conv={}
for i in range(65,91):
    conv[chr(i)]=i-65

for i in range(97,123):
    conv[chr(i)]=i-71

N,M,T,D=map(int,input().split())
mat=[input().rstrip() for i in range(N)]
matrix=[[conv[w] for w in mat[i]] for i in range(N)]
vi=[[inf for i in range(M)]for i in range(N)]
rvi=[[inf for i in range(M)]for i in range(N)]
rvi[0][0]=0
queue=[[0,0,0]] # 누적 시간, 높이, 좌표
ans=matrix[0][0]

while queue:
    t,x,y=heappop(queue)
    if vi[y][x]<t:
        continue
    vi[y][x]=t
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<M and -1<ny<N:
            dxy=matrix[ny][nx]-matrix[y][x]
            if dxy>T:
                continue
            dt=1 if matrix[ny][nx] <= matrix[y][x] else (dxy)**2
            if t+dt>D:
                continue
            if vi[ny][nx]<=t+dt:
                continue
            vi[ny][nx]=t+dt
            heappush(queue,[t+dt,nx,ny])

queue=[[0,0,0]]

while queue:
    t,x,y=heappop(queue)
    if rvi[y][x]<t:
        continue
    rvi[y][x]=t
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<M and -1<ny<N:
            dxy=matrix[ny][nx]-matrix[y][x]
            if dxy>T:
                continue
            dt=1 if matrix[ny][nx] >= matrix[y][x] else (dxy)**2
            if t+dt>D:
                continue
            if rvi[ny][nx]<=t+dt:
                continue
            rvi[ny][nx]=t+dt
            heappush(queue,[t+dt,nx,ny])

for i in range(N):
    for j in range(M):
        totaltime=vi[i][j]+rvi[i][j]
        if totaltime<=D:
            ans=max(ans,matrix[i][j])

print(ans)

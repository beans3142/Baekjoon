from sys import stdin
from collections import deque
input=stdin.readline

# 모델링
inf=float('inf')

n,m=map(int,input().split())

MXN=100
MXV=2*MXN+2
S=MXV-2
E=MXV-1

c=[[0]*MXV for j in range(MXV)]
d=[[0]*MXV for j in range(MXV)]
f=[[0]*MXV for j in range(MXV)]

adj=[[] for i in range(MXV)]

arr=list(map(int,input().split()))

for i in range(MXN,MXN+n):
    c[i][E]=arr[i-MXN]
    adj[E].append(i)
    adj[i].append(E)

arr=list(map(int,input().split()))

for i in range(m):
    c[S][i]=arr[i]
    adj[S].append(i)
    adj[i].append(S)

for i in range(m):
    arr=list(map(int,input().split()))
    for j in range(MXN,MXN+n):
        c[i][j]=arr[j-MXN]
        c[j][i]=-c[i][j]

for i in range(m):
    arr=list(map(int,input().split()))
    for j in range(MXN,MXN+n):
        d[i][j]=arr[j-MXN]
        d[j][i]=-d[i][j]
        #c[i][j]=inf
        adj[i].append(j)
        adj[j].append(i)

# 최소 비용
res=0
cnt=0

# 아래 부분이 MCMF
while True:
    prev=[-1]*MXV
    dist=[inf]*MXV
    inQ=[False]*MXV
    queue=deque([S])
    dist[S]=0
    inQ[S]=True
    while queue:
        now=queue.popleft()
        inQ[now]=False
        for nxt in adj[now]:
            if c[now][nxt]-f[now][nxt]>0 and dist[nxt]>dist[now]+d[now][nxt]:
                dist[nxt]=dist[now]+d[now][nxt]
                prev[nxt]=now
                if inQ[nxt]==0:
                    inQ[nxt]=True
                    queue.append(nxt)
    
    if prev[E]==-1:
        break

    flow=inf
    i=E
    while i!=S:
        flow=min(flow,c[prev[i]][i]-f[prev[i]][i])
        i=prev[i]
    i=E
    while i!=S:
        res+=flow*d[prev[i]][i]
        f[prev[i]][i]+=flow
        f[i][prev[i]]-=flow
        i=prev[i]
    cnt+=flow

print(cnt)
print(res)

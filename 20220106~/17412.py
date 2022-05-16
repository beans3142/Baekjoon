from sys import stdin
from collections import deque
input=stdin.readline

# 모델링
inf=float('inf')

n,p=map(int,input().split())

MXN=400
MXV=2*MXN+2
S=1
E=2

c=[[0]*MXV for j in range(MXV)]
f=[[0]*MXV for j in range(MXV)]

adj=[[] for i in range(MXV)]

for i in range(1,n+1):
    adj[i].append(i+MXN)
    adj[i+MXN].append(i)
    c[i][i+MXN]=1

for i in range(p):
    a,b=map(int,input().split())
    adj[b].append(a)
    adj[a].append(b)
    
    c[a][b]=1

# 최소 비용
cnt=0

# 아래 부분이 MCMF
while True:
    prev=[-1]*MXV

    queue=deque([S])
    prev[S]=-1
    
    while queue:
        now=queue.popleft()
        for nxt in adj[now]:
            if c[now][nxt]-f[now][nxt]>0 and prev[nxt]==-1:
                prev[nxt]=now
                queue.append(nxt)
                if nxt==2:
                    break
    
    if prev[E]==-1:
        break

    flow=inf
    i=E
    while i!=S:
        flow=min(flow,c[prev[i]][i]-f[prev[i]][i])
        i=prev[i]
    i=E
    while i!=S:
        f[prev[i]][i]+=flow
        f[i][prev[i]]-=flow
        i=prev[i]
    cnt+=flow

print(cnt)

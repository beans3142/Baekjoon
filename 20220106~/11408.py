from sys import stdin
from collections import deque
input=stdin.readline

# 모델링
inf=float('inf')

n,m=map(int,input().split())

MXN=400
MXV=MXN*2+2
S=MXV-2
E=MXV-1

c=[[0]*MXV for j in range(MXV)]
d=[[0]*MXV for j in range(MXV)]
f=[[0]*MXV for j in range(MXV)]

adj=[[] for i in range(MXV)]

for i in range(1,n+1):
    c[0][i]=1
    adj[0].append(i)
    adj[i].append(0)

for i in range(1,m+1):
    c[MXN+i][E]=1
    adj[E].append(i+MXN)
    adj[i+MXN].append(E)

for i in range(1,n+1):
    li=list(map(int,input().split()))
    for j in range(li[0]):
        workno=li[1+j*2]
        workpay=li[1+j*2+1]

        adj[i].append(MXN+workno)
        adj[MXN+workno].append(i)

        d[i][MXN+workno]=workpay
        d[workno+MXN][i]=-workpay

        c[i][MXN+workno]=1

# 최소 비용
res=0
# 최소 인원
cnt=0

# 아래 부분이 MCMF
while True:
    prev=[-1]*MXV
    dist=[inf]*MXV
    inQ=[False]*MXV
    queue=deque([0])
    dist[0]=0
    inQ[0]=True
    prev[0]=0
    
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
    while i!=0:
        flow=min(flow,c[prev[i]][i]-f[prev[i]][i])
        i=prev[i]
    i=E
    while i!=0:
        res+=flow*d[prev[i]][i]
        f[prev[i]][i]+=1
        f[i][prev[i]]-=1
        i=prev[i]

    cnt+=1

print(cnt)
print(res)

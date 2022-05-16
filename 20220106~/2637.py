from sys import stdin
from collections import deque
input=stdin.readline

def leveling():
    global lv
    lv=[-1]*MXV
    queue=deque([(S,0)])
    lv[S]=0
    
    while queue:
        now,nowlv=queue.popleft()
        for nxt in adj[now]:
            if c[now][nxt]-f[now][nxt]>0 and lv[nxt]==-1:
                lv[nxt]=nowlv+1
                queue.append([nxt,lv[nxt]])

    return lv[E]!=-1

def dfs(now,flow):
    if now==E:
        return flow
    for nxt in adj[now]:
        if lv[nxt]==lv[now]+1 and c[now][nxt]-f[now][nxt]>0:
            nowflow=dfs(nxt,min(flow,c[now][nxt]-f[now][nxt]))
            if nowflow>0:
                f[now][nxt]+=nowflow
                f[nxt][now]-=nowflow
                return nowflow
    return 0

# 모델링
inf=float('inf')

n,k,d=map(int,input().split())

MXN=200
MXV=302
S=0
E=301

lv=[-1]*MXV
c=[[0]*MXV for j in range(MXV)]
f=[[0]*MXV for j in range(MXV)]

adj=[[] for i in range(MXV)]

arr=list(map(int,input().split()))
for i in range(1,d+1):
    adj[E].append(i+MXN)
    adj[i+MXN].append(E)
    c[i+MXN][E]=arr[i-1]

for i in range(1,n+1):
    arr=list(map(int,input().split()))
    adj[S].append(i)
    adj[i].append(S)
    c[S][i]=k
    le=arr[0]
    for j in range(1,le+1):
        adj[i].append(arr[j]+MXN)
        adj[arr[j]+MXN].append(i)
        c[i][arr[j]+MXN]=1

# 최소 비용
cnt=0

while leveling():
    while True:
        flow=dfs(S,inf)
        if not flow:
            break
        cnt+=flow

print(cnt)

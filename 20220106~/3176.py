from sys import stdin
from collections import *
input=stdin.readline

def bfs(r):
    queue=deque([(r,0)])
    while queue:
        now,dep=queue.popleft()
        depth[now]=dep
        for i in tree[now]:
            if depth[i]==-1:
                par[i][0]=now
                dist[i][0][0]=dist[i][0][1]=tree[now][i]
                queue.append((i,dep+1))

def lca(a,b):
    if depth[a]>depth[b]:
        a,b=b,a
    for i in range(log-1,-1,-1):
        if depth[b]-depth[a]>=(1<<i):
            b=par[b][i]
    if a==b:
        return a
    for i in range(log-1,-1,-1):
        if par[a][i]!=par[b][i]:
            a=par[a][i]
            b=par[b][i]

    return par[a][0]

log=18
n=int(input())
par=[[0 for i in range(log)] for i in range(n+1)]
dist=[[[10**10,-10**10] for i in range(log)] for i in range(n+1)]
tree=[defaultdict(int) for i in range(n+1)]
depth=[-1]*(n+1)

for i in range(n-1):
    a,b,c=map(int,input().split())
    tree[a][b]=tree[b][a]=c

bfs(1)
for i in range(1,log):
    for j in range(1,n+1):
        par[j][i]=par[par[j][i-1]][i-1]
        dist[j][i][0]=min(dist[j][i][0],dist[par[j][i-1]][i-1][0])
        dist[j][i][1]=max(dist[j][i][1],dist[par[j][i-1]][i-1][1])

k=int(input())
for i in range(k):
    a,b=map(int,input().split())
    print(lca(a,b))

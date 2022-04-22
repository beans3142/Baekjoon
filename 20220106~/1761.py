from sys import stdin
from collections import defaultdict,deque
input=stdin.readline

n=int(input())
par=[0]*(n+1)
depth=[-1]*(n+1)
dists=[-1]*(n+1)
vi=[0]*(n+1)
tree=[defaultdict(int) for i in range(n+1)]

for i in range(n-1):
    a,b,c=map(int,input().split())
    tree[a][b]=c
    tree[b][a]=c
    
def bfs(r):
    queue=deque([(r,0,0)])
    while queue:
        now,dep,dist=queue.popleft()
        vi[now]=1
        depth[now]=dep
        dists[now]=dist
        for i in tree[now]:
            if vi[i]==1:
                continue
            par[i]=now
            queue.append((i,dep+1,dist+tree[now][i]))

def lca(a,b):
    dist=0
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=par[a]
        else:
            b=par[b]
    while a!=b:
        a=par[a]
        b=par[b]
    return a

m=int(input())
bfs(1)
for i in range(m):
    a,b=map(int,input().split())
    LCA=lca(a,b)
    print(dists[a]+dists[b]-2*dists[LCA])

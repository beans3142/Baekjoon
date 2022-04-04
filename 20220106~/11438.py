from sys import stdin
from collections import defaultdict,deque
input=stdin.readline
log=21

n=int(input())
par=[[0 for i in range(log)] for i in range(n+1)]
depth=[-1]*(n+1)
vi=[0]*(n+1)
tree=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def bfs(r):
    queue=deque([(r,0)])
    while queue:
        now,dep=queue.popleft()
        vi[now]=1
        depth[now]=dep
        for i in tree[now]:
            if vi[i]==1:
                continue
            par[i][0]=now
            queue.append((i,dep+1))

def lca(a,b):
    if depth[a]>depth[b]:
        a,b=b,a
    for i in range(log-1,-1,-1):
        if depth[b]-depth[a]>=(1<<i):
            b=par[b][i] # 올라가는 속도를 매우 빠르게, 1칸씩이 아니라
    if a==b:
        return a
    for i in range(log-1,-1,-1):
        if par[a][i]!=par[b][i]:
            a=par[a][i]
            b=par[b][i]
    return par[a][0]

def setpar():
    bfs(1)
    for i in range(1,log):
        for j in range(1,n+1):
            par[j][i]=par[par[j][i-1]][i-1]

m=int(input())
setpar()
for i in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))

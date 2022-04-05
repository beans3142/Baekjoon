from sys import stdin
from collections import defaultdict,deque
input=stdin.readline

n,x,y=map(int,input().split())
par=[0]*(n)
depth=[-1]*(n)
vi=[0]*(n)
tree=[[] for i in range(n)]

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
            par[i]=now
            queue.append((i,dep+1))

def lca(a,b):
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=par[a]
        else:
            b=par[b]
    while a!=b:
        a=par[a]
        b=par[b]
    return a

bfs(0)

print(lca(x,y))

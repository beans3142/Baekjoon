from sys import stdin
from collections import deque
input=stdin.readline

log=23

def bfs(x):
    depth[x]=0
    queue=deque([x])

    while queue:
        now=queue.popleft()
        for i in tree[now]:
            if depth[i]==-1:
                depth[i]=depth[now]+1
                par[0][i]=now
                queue.append(i)
    

def lca(a,b):
    cnt=1
    if depth[a]>depth[b]:
        a,b=b,a
    for i in range(log-1,-1,-1):
        if depth[b]-depth[a]>=(1<<i):
            cnt+=1<<i
            b=par[i][b]
    if a==b:
        return cnt
    for i in range(log-1,-1,-1):
        if par[i][a]!=par[i][b]:
            a=par[i][a]
            b=par[i][b]
            cnt+=1<<(i+1)
    if a!=b:
        cnt+=2
    return cnt

n=int(input())
tree=[[] for i in range(n+1)]
depth=[-1]*(n+1)
par=[[0]*(n+1) for i in range(log)]

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs(1)

for i in range(1,log):
    for j in range(1,n+1):
        par[i][j]=par[i-1][par[i-1][j]]

ans=0

for i in range(1,n+1):
    for j in range(i+i,n+1,i):
        ans+=lca(i,j)

print(ans)
    

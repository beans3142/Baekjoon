from sys import stdin
from collections import deque
input=stdin.readline

log=20


def bfs(x):
    queue=deque([x])
    depth[x]=0
    par[x][0]=0
    while queue:
        now=queue.popleft()
        for i in tree[now]:
            if depth[i]==-1:
                depth[i]=depth[now]+1
                par[0][i]=now
                queue.append(i)

def lca(a,b):
    global ans
    if depth[a]>depth[b]:
        a,b=b,a
    for i in range(log-1,-1,-1):
        if depth[b]-depth[a]>=(1<<i):
            ans+=1<<i
            b=par[i][b]
    if a==b:
        return a
    for i in range(log-1,-1,-1):
        if par[i][a]!=par[i][b]:
            a=par[i][a]
            b=par[i][b]
            ans+=1<<(i+1)
    if a!=b:
        ans+=2
    return par[0][a]
            
        

n=int(input())
tree=[[] for i in range(n+1)]
depth=[-1]*(n+1)

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

ans=0
par=[[0 for i in range(n+1)] for i in range(log)]
   
bfs(1)

for i in range(1,log):
    for j in range(1,n+1):
        par[i][j]=par[i-1][par[i-1][j]]

j=int(input())
now=int(input())
for i in range(j-1):
    nxt=int(input())
    lca(now,nxt)
    now=nxt

print(ans)

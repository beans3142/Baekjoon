from sys import stdin
from collections import *
input=stdin.readline

def bfs(r):
    queue=deque([(r,0)])
    while queue:
        now,dep=queue.popleft()
        depth[now]=dep
        for i in graph[now]:
            if depth[i]!=-1:
                continue
            par[i]=now
            queue.append((i,dep+1))

def lca(a,b):
    cnt=0
    while depth[a]>depth[b]:
        a=par[a]
        cnt+=1
    while depth[b]>depth[a]:
        b=par[b]
        cnt+=1
    while a!=b:
        a=par[a]
        b=par[b]
        cnt+=2
    return cnt

t=int(input())

for _ in range(t):
    able=1
    n=int(input())
    graph=[[] for i in range(n+1)]
    depth=[-1 for i in range(n+1)]
    par=[0 for i in range(n+1)]
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    bfs(1)
    first=int(input())
    for i in range(n-1):
        second=int(input())
        if able==0:
            continue
        cnt=lca(first,second)
        if cnt>3:
            able=0
        first=second
    print(able)
    

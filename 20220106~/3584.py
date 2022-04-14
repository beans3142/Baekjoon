from sys import stdin
from collections import deque
input=stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    graph=[[] for i in range(n+1)]
    par=[0]*(n+1)
    depth=[-1]*(n+1)
    for i in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        par[b]=(a)

    for i in range(1,n+1):
        if not par[i]:
            queue=deque([(i,0)])
            depth[i]=0
            break
    
    while queue:
        now,dep=queue.popleft()
        for i in graph[now]:
            if depth[i]==-1:
                depth[i]=dep+1
                queue.append((i,dep+1))
                

    a,b=map(int,input().split())
    while depth[b]<depth[a]:
        a=par[a]
    while depth[a]<depth[b]:
        b=par[b]
    while a!=b:
        a=par[a]
        b=par[b]
    
    print(a)

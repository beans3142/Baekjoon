from sys import stdin
from collections import deque
input=stdin.readline
k=int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[] for i in range(v+1)]
    for i in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    vi=[-1]*(v+1)
    div=True
    for i in range(1,v+1):
        if vi[i]!=-1:continue
        vi[i]=0
        q=deque([i])
        while q:
            now=q.popleft()
            for nxt in graph[now]:
                if vi[nxt]==vi[now]:
                    div=False
                elif vi[nxt]==-1:
                    vi[nxt]=1-vi[now]
                    q.append(nxt)
    if div:
        print("YES")
    else:
        print("NO")
